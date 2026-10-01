"""Browser session management and Suno generation via Playwright + CDP."""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Any

from playwright.async_api import BrowserContext, Page, async_playwright

from .config import BROWSER_PROFILE_DIR, CDP_URL, DEBUG, HEADLESS, SUNO_CREATE_URL

CDP_RECONNECT_URL = "http://127.0.0.1:9222"
_LAUNCH_ARGS = [
    "--disable-blink-features=AutomationControlled",
    f"--remote-debugging-port=9222",
]

logger = logging.getLogger(__name__)

# Ported from unforced/suno-mcp — drives React state then trusted CDP click for hCaptcha.
_PREPARE_GENERATE_JS = """
async (payload) => {
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));

  function walkUp(el, match, maxDepth = 40) {
    const fkey = Object.keys(el).find(k => k.startsWith('__reactFiber$'));
    if (!fkey) return null;
    let f = el[fkey], d = 0;
    while (f && d < maxDepth) {
      if (match(f)) return f;
      f = f.return; d++;
    }
    return null;
  }

  function setReactValue(el, value) {
    const proto = el instanceof HTMLTextAreaElement
      ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
    const setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
    setter.call(el, value);
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }

  const anchor = document.querySelector('button[aria-label="Create song"]')
    || document.querySelector('main') || document.body;
  const createFiber = walkUp(anchor, f =>
    f.memoizedProps && typeof f.memoizedProps.onCreateClick === 'function'
  );
  if (!createFiber) {
    return { success: false, error: 'Could not locate generate handler (onCreateClick) in React fiber.' };
  }

  const cp = createFiber.memoizedProps;
  if (cp.isGenerating) {
    return { success: false, error: 'A generation is already in progress. Wait for it to finish.' };
  }
  if (cp.isOutOfCredits) {
    return { success: false, error: 'Out of credits.' };
  }

  const wantMode = payload.mode === 'simple' ? 'simple' : 'custom';
  if (cp.mode && cp.mode !== wantMode) {
    const tabLabel = wantMode === 'simple' ? 'Simple' : 'Advanced';
    const tabBtn = Array.from(document.querySelectorAll('button[role="tab"], [role="tab"]')).find(b => {
      const label = (b.getAttribute('aria-label') || b.textContent || '').trim().toLowerCase();
      return label === tabLabel.toLowerCase();
    });
    if (tabBtn) { tabBtn.click(); await sleep(800); }
  }

  if (payload.mode === 'custom') {
    const lyricsArea = document.querySelector('textarea[data-testid="lyrics-textarea"]')
      || Array.from(document.querySelectorAll('textarea')).find(t =>
        /lyric|write/i.test(t.placeholder || ''));
    if (!lyricsArea) return { success: false, error: 'Lyrics textarea not found.' };
    setReactValue(lyricsArea, payload.lyrics);

    let styleArea = document.querySelector(
      'textarea[maxlength="1000"]:not([data-testid="lyrics-textarea"])'
    );
    if (!styleArea) {
      styleArea = Array.from(document.querySelectorAll('textarea')).find(t =>
        t !== lyricsArea && !t.closest('[style*="display: none"]'));
    }
    if (!styleArea) return { success: false, error: 'Style textarea not found.' };
    setReactValue(styleArea, payload.style);
  } else {
    const promptArea = document.querySelector('textarea[data-testid="prompt-textarea"]')
      || document.querySelector('textarea');
    if (!promptArea) return { success: false, error: 'Simple-mode prompt textarea not found.' };
    setReactValue(promptArea, payload.simplePrompt);
  }

  async function waitForFiberSync(attempts = 20) {
    for (let i = 0; i < attempts; i++) {
      const fresh = walkUp(
        document.querySelector('button[aria-label="Create song"]') || anchor,
        f => f.memoizedProps && typeof f.memoizedProps.onCreateClick === 'function'
      );
      if (!fresh) { await sleep(150); continue; }
      const p = fresh.memoizedProps;
      const ok = payload.mode === 'custom'
        ? (p.lyrics && p.lyrics.length > 0 && p.styles && (
            Array.isArray(p.styles) ? p.styles.length > 0 : String(p.styles).length > 0
          ))
        : (p.lyrics && p.lyrics.length > 0) || (p.simplePrompt && p.simplePrompt.length > 0);
      if (ok) return { fiber: fresh, waited: i * 150 };
      await sleep(150);
    }
    return { fiber: null };
  }

  const synced = await waitForFiberSync();
  const btnEl = document.querySelector('button[aria-label="Create song"]');
  if (!btnEl) return { success: false, error: 'Create button not in DOM.' };
  btnEl.scrollIntoView({ block: 'center' });
  await sleep(100);
  const r = btnEl.getBoundingClientRect();
  if (r.width === 0 || r.height === 0) {
    return { success: false, error: 'Create button has zero size (not visible). Use SUNO_HEADLESS=false.' };
  }
  return {
    success: true,
    clickX: r.left + r.width / 2,
    clickY: r.top + r.height / 2,
    waitedMs: synced.waited || 0,
    useDirectHandler: true,
  };
}
"""

_DISMISS_OVERLAYS_JS = """
async () => {
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));
  let dismissed = 0;
  const allowAll = document.querySelector('#accept-recommended-btn-handler');
  if (allowAll) { allowAll.click(); dismissed++; await sleep(400); }
  const closePrefs = document.querySelector('#close-pc-btn-handler');
  if (closePrefs) { closePrefs.click(); dismissed++; await sleep(200); }
  for (const label of ['Accept All', 'Allow All', 'Reject All', 'Close']) {
    const btn = Array.from(document.querySelectorAll('button')).find(b =>
      (b.textContent || '').trim() === label
    );
    if (btn) { btn.click(); dismissed++; await sleep(200); }
  }
  return { dismissed };
}
"""

_INVOKE_CREATE_JS = """
async () => {
  function walkUp(el, match, maxDepth = 40) {
    const fkey = Object.keys(el).find(k => k.startsWith('__reactFiber$'));
    if (!fkey) return null;
    let f = el[fkey], d = 0;
    while (f && d < maxDepth) {
      if (match(f)) return f;
      f = f.return; d++;
    }
    return null;
  }
  const anchor = document.querySelector('button[aria-label="Create song"]')
    || document.querySelector('main') || document.body;
  const fiber = walkUp(anchor, f =>
    f.memoizedProps && typeof f.memoizedProps.onCreateClick === 'function'
  );
  if (!fiber) return { ok: false, error: 'Create handler not found' };
  try {
    await fiber.memoizedProps.onCreateClick();
    return { ok: true };
  } catch (e) {
    return { ok: false, error: e && e.message || String(e) };
  }
}
"""

_GET_TOKEN_JS = """
async () => {
  if (!window.Clerk) return { error: 'Clerk not loaded yet. Open https://suno.com/create and sign in.' };
  if (!window.Clerk.session) return { error: 'Not signed in to Suno. Log in via the browser window.' };
  try {
    const token = await window.Clerk.session.getToken();
    return { ok: true, token };
  } catch (e) {
    return { error: e && e.message || String(e) };
  }
}
"""


class BrowserSession:
    """Manages a persistent Playwright browser with Suno logged in."""

    def __init__(self) -> None:
        self._playwright = None
        self._context: BrowserContext | None = None
        self._page: Page | None = None
        self._lock = asyncio.Lock()

    async def get_page(self) -> Page:
        async with self._lock:
            if self._page and not self._page.is_closed():
                return self._page
            await self._ensure_browser()
            assert self._page is not None
            return self._page

    async def _ensure_browser(self) -> None:
        if self._context and self._page and not self._page.is_closed():
            return

        self._playwright = await async_playwright().start()
        BROWSER_PROFILE_DIR.mkdir(parents=True, exist_ok=True)

        cdp_url = CDP_URL or CDP_RECONNECT_URL
        try:
            if CDP_URL:
                browser = await self._playwright.chromium.connect_over_cdp(cdp_url)
                if browser.contexts:
                    self._context = browser.contexts[0]
                else:
                    self._context = await browser.new_context()
            else:
                self._context = await self._playwright.chromium.launch_persistent_context(
                    user_data_dir=str(BROWSER_PROFILE_DIR),
                    headless=HEADLESS,
                    args=_LAUNCH_ARGS,
                    viewport={"width": 1280, "height": 900},
                )
        except Exception as exc:
            if "already in use" in str(exc).lower() or "existing browser session" in str(exc).lower():
                browser = await self._playwright.chromium.connect_over_cdp(cdp_url)
                if browser.contexts:
                    self._context = browser.contexts[0]
                else:
                    self._context = await browser.new_context()
            else:
                raise

        pages = self._context.pages
        self._page = pages[0] if pages else await self._context.new_page()

        if "/create" not in self._page.url:
            await self._page.goto(SUNO_CREATE_URL, wait_until="domcontentloaded")
            await asyncio.sleep(2)

        try:
            await self._page.evaluate(_DISMISS_OVERLAYS_JS)
        except Exception:
            pass

    async def get_token(self) -> str:
        page = await self.get_page()
        if "/create" not in page.url:
            await page.goto(SUNO_CREATE_URL, wait_until="domcontentloaded")
            await asyncio.sleep(1.5)

        last_error = "Not signed in to Suno. Log in via the browser window."
        for _ in range(15):
            result = await page.evaluate(_GET_TOKEN_JS)
            if result.get("error"):
                last_error = result["error"]
                await asyncio.sleep(1)
                continue
            token = result.get("token")
            if token:
                return token
            await asyncio.sleep(1)

        raise RuntimeError(last_error)

    async def _cdp_click(self, page: Page, x: float, y: float) -> None:
        cdp = await page.context.new_cdp_session(page)
        try:
            await cdp.send("Input.dispatchMouseEvent", {
                "type": "mouseMoved", "x": x, "y": y, "button": "none", "buttons": 0,
            })
            await cdp.send("Input.dispatchMouseEvent", {
                "type": "mousePressed", "x": x, "y": y, "button": "left", "buttons": 1, "clickCount": 1,
            })
            await asyncio.sleep(0.04)
            await cdp.send("Input.dispatchMouseEvent", {
                "type": "mouseReleased", "x": x, "y": y, "button": "left", "buttons": 0, "clickCount": 1,
            })
        finally:
            await cdp.detach()

    async def _click_create(self, page: Page, prep: dict[str, Any]) -> str:
        """Try trusted CDP click first (hCaptcha), then Playwright, then React handler."""
        x, y = prep["clickX"], prep["clickY"]

        await self._cdp_click(page, x, y)
        if DEBUG:
            logger.info("Clicked Create via CDP at (%s, %s)", x, y)
        return "cdp"

    async def _click_create_fallbacks(self, page: Page, prep: dict[str, Any]) -> str:
        create_btn = page.locator('button[aria-label="Create song"]')
        if await create_btn.count():
            await create_btn.click(timeout=5000)
            if DEBUG:
                logger.info("Clicked Create via Playwright locator")
            return "playwright"

        invoked = await page.evaluate(_INVOKE_CREATE_JS)
        if invoked.get("ok"):
            if DEBUG:
                logger.info("Invoked onCreateClick directly (fallback)")
            return "react-handler"

        raise RuntimeError(invoked.get("error") or "Could not click Create")

    async def drive_generate(self, *, mode: str, lyrics: str = "", style: str = "", simple_prompt: str = "") -> dict[str, Any]:
        page = await self.get_page()
        if "/create" not in page.url:
            await page.goto(SUNO_CREATE_URL, wait_until="domcontentloaded")
            await asyncio.sleep(1.5)

        await page.evaluate(_DISMISS_OVERLAYS_JS)

        payload = {
            "mode": mode,
            "lyrics": lyrics,
            "style": style,
            "simplePrompt": simple_prompt,
        }

        captured_clips: list[dict] = []
        capture_event = asyncio.Event()

        async def on_response(response):
            if "studio-api" not in response.url and "/api/generate/" not in response.url:
                return
            if DEBUG:
                logger.info("Suno API response: %s %s", response.status, response.url)
            if "/api/generate/" not in response.url or response.status != 200:
                return
            try:
                data = await response.json()
                clips = data.get("clips") or (data.get("data") or {}).get("clips")
                if clips:
                    captured_clips.extend(clips)
                    capture_event.set()
            except Exception:
                logger.debug("Failed to parse generate response from %s", response.url, exc_info=True)

        page.on("response", on_response)

        try:
            prep = await page.evaluate(_PREPARE_GENERATE_JS, payload)
            if not prep.get("success"):
                raise RuntimeError(prep.get("error", "Failed to prepare generation"))

            if DEBUG:
                logger.info("Prepared generate: %s", prep)

            click_method = await self._click_create(page, prep)
            try:
                await asyncio.wait_for(capture_event.wait(), timeout=15)
            except asyncio.TimeoutError:
                if DEBUG:
                    logger.warning("CDP click did not start generation; trying fallbacks")
                click_method = await self._click_create_fallbacks(page, prep)
                try:
                    await asyncio.wait_for(capture_event.wait(), timeout=30)
                except asyncio.TimeoutError:
                    logger.warning("No /api/generate/ response captured within 45s (method=%s)", click_method)

            if captured_clips:
                return {
                    "clips": captured_clips,
                    "message": "Song generation started",
                    "click_method": click_method,
                }

            return {
                "clips": [],
                "message": "Create was clicked but no generate API response was captured. "
                "Check the Suno browser window for hCaptcha or UI errors.",
                "prepared": prep,
                "click_method": click_method,
            }
        finally:
            page.remove_listener("response", on_response)

    async def close(self) -> None:
        if self._context:
            await self._context.close()
            self._context = None
            self._page = None
        if self._playwright:
            await self._playwright.stop()
            self._playwright = None


_session: BrowserSession | None = None


def get_browser_session() -> BrowserSession:
    global _session
    if _session is None:
        _session = BrowserSession()
    return _session
