"""Get Suno JWT token using Playwright (no MCP dependency)."""

import asyncio
from playwright.async_api import async_playwright

# Read cookie
env = {}
with open(".env", encoding="utf-8") as f:
    for line in f:
        if line.startswith("SUNO_COOKIE="):
            cookie_str = line.split("=", 1)[1].strip().strip('"').strip("'")
            break

print(f"Cookie string length: {len(cookie_str)}")
print(f"First 100 chars: {cookie_str[:100]}...")


async def main():
    # Launch headless browser
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--remote-debugging-port=9222",
            ],
        )

        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="en-US",
        )

        # Set cookies
        for part in cookie_str.split(";"):
            part = part.strip()
            if "=" in part:
                k, v = part.split("=", 1)
                k = k.strip()
                v = v.strip()
                if k == "__client" or k == "__session":
                    await context.add_cookies(
                        [{"name": k, "value": v, "url": "https://suno.com"}]
                    )

        # Go to Suno and get token from localStorage
        page = await context.new_page()
        await page.goto("https://suno.com/")
        await page.wait_for_timeout(5000)  # Wait for page to load

        # Try to get token from localStorage
        try:
            token = await page.evaluate("""
                () => {
                    const client = localStorage.getItem('__client');
                    const session = localStorage.getItem('__session');
                    return { client, session };
                }
            """)
            print(f"Token from localStorage:")
            print(
                f"  __client: {token['client'][:50]}..."
                if token["client"]
                else "  __client: N/A"
            )
            print(
                f"  __session: {token['session'][:50]}..."
                if token["session"]
                else "  __session: N/A"
            )

            # If we have the client token, we can use it directly
            if token["client"]:
                print("\nUsing __client token for API auth")
                # Now fetch clips using this token
                import httpx
                import json, time

                session = httpx.Client(
                    base_url="https://studio-api.prod.suno.com",
                    timeout=60.0,
                    verify=False,
                    headers={
                        "Authorization": f"Bearer {token['client']}",
                        "Content-Type": "application/json",
                    },
                )

                all_clips = []
                page_num = 1

                while True:
                    resp = session.get(
                        "/api/feed/v2", params={"page": page_num, "page_size": 50}
                    )
                    if resp.status_code != 200:
                        print(f"Page {page_num}: HTTP {resp.status_code}")
                        break

                    data = resp.json()
                    clips = data.get("clips", [])
                    if not clips:
                        break

                    for c in clips:
                        proj = c.get("project") or {}
                        all_clips.append(
                            {
                                "id": c.get("id"),
                                "title": c.get("title"),
                                "status": c.get("status"),
                                "created_at": c.get("created_at"),
                                "model_name": c.get("model_name"),
                                "project_id": proj.get("id")
                                if isinstance(proj, dict)
                                else None,
                                "project_name": proj.get("name")
                                if isinstance(proj, dict)
                                else None,
                                "duration": (c.get("metadata") or {}).get("duration"),
                            }
                        )

                    print(
                        f"  Page {page_num}: {len(clips)} clips (total: {len(all_clips)})"
                    )
                    page_num += 1
                    await asyncio.sleep(1.5)

                print(f"\n  Fetched {len(all_clips)} clips!")
                session.close()
        except Exception as e:
            print(f"Error: {e}")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
