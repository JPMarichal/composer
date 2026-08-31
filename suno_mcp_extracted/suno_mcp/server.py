"""Suno MCP Server — uses your suno.com account via browser session."""

import atexit
import asyncio
import json
import os
import sys

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

from .client import get_client

load_dotenv()

mcp = FastMCP("suno_mcp")


def _json(data) -> str:
    return json.dumps(data, indent=2, default=str)


class GenerateSongInput(BaseModel):
    lyrics: str = Field(description="Song lyrics with section tags like [Verse], [Chorus]")
    style: str = Field(description="Style tags, e.g. 'indie folk, acoustic, male vocals'")


class GenerateFromDescriptionInput(BaseModel):
    description: str = Field(description="Describe the song; Suno writes lyrics automatically")


class SongIdsInput(BaseModel):
    song_ids: list[str] = Field(description="Suno clip/song IDs to check or wait on")


class DownloadSongInput(BaseModel):
    song_id: str = Field(description="Suno clip/song ID")
    folder: str = Field(default="~/Downloads/suno", description="Folder to save the MP3")
    filename: str | None = Field(default=None, description="Optional filename without extension")


class RecentSongsInput(BaseModel):
    page: int = Field(default=1, ge=1, description="Page number for recent songs")


@mcp.tool(name="suno_get_credits")
async def suno_get_credits() -> str:
    """Check your Suno account credit balance (uses your logged-in suno.com session)."""
    return _json(await get_client().get_credits())


@mcp.tool(name="suno_get_recent")
async def suno_get_recent(params: RecentSongsInput) -> str:
    """List your recent Suno songs from your account library."""
    return _json(await get_client().get_recent_songs(page=params.page))


@mcp.tool(name="suno_generate_song")
async def suno_generate_song(params: GenerateSongInput) -> str:
    """
    Generate a song with custom lyrics and style (Custom Mode).

    Opens/uses a browser with your Suno login. Generation runs through suno.com
    so no third-party API is needed. Returns clip IDs — use suno_wait_for_songs to poll.
    """
    result = await get_client().generate_song(lyrics=params.lyrics, style=params.style)
    clips = result.get("clips") or []
    song_ids = [c.get("id") for c in clips if c.get("id")]
    return _json({
        "message": result.get("message"),
        "song_ids": song_ids,
        "clips": clips,
    })


@mcp.tool(name="suno_generate_from_description")
async def suno_generate_from_description(params: GenerateFromDescriptionInput) -> str:
    """
    Generate a song from a text description (Simple/Inspiration Mode).
    Suno writes the lyrics automatically.
    """
    result = await get_client().generate_from_description(params.description)
    clips = result.get("clips") or []
    song_ids = [c.get("id") for c in clips if c.get("id")]
    return _json({
        "message": result.get("message"),
        "song_ids": song_ids,
        "clips": clips,
    })


@mcp.tool(name="suno_check_status")
async def suno_check_status(params: SongIdsInput) -> str:
    """Check generation status for one or more song IDs."""
    return _json(await get_client().get_song_status(params.song_ids))


@mcp.tool(name="suno_wait_for_songs")
async def suno_wait_for_songs(params: SongIdsInput) -> str:
    """Wait until songs finish generating (up to 3 minutes), then return audio URLs."""
    songs = await get_client().wait_for_songs(params.song_ids)
    return _json({"songs": songs})


@mcp.tool(name="suno_download_song")
async def suno_download_song(params: DownloadSongInput) -> str:
    """Download a completed song as MP3 to a local folder."""
    return _json(await get_client().download_song(
        params.song_id,
        params.folder,
        params.filename,
    ))


def main() -> None:
    if os.getenv("SUNO_HEADLESS", "false").lower() in ("1", "true", "yes"):
        print(
            "Warning: SUNO_HEADLESS=true may break generation (Create button must be visible).",
            file=sys.stderr,
        )

    def _cleanup():
        try:
            client = get_client()
            asyncio.get_event_loop().run_until_complete(client.close())
        except Exception:
            pass

    atexit.register(_cleanup)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
