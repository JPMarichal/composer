"""Configuration for Suno MCP."""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SUNO_API_BASE = "https://studio-api.prod.suno.com"
SUNO_CREATE_URL = "https://suno.com/create"

_default_profile = Path.home() / ".suno-mcp" / "browser-profile"
_profile = os.getenv("SUNO_BROWSER_PROFILE_DIR", str(_default_profile))
BROWSER_PROFILE_DIR = Path(_profile).expanduser()

HEADLESS = os.getenv("SUNO_HEADLESS", "false").lower() in ("1", "true", "yes")
CDP_URL = os.getenv("SUNO_CDP_URL", "").strip() or None
DEBUG = os.getenv("SUNO_DEBUG", "").lower() in ("1", "true", "yes")
