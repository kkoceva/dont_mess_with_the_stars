"""Game settings and constants."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
TEXTURES_DIR = ASSETS_DIR / "textures"

TILE_SIZE = 40

UI_PANEL_HEIGHT = 80

MAP_WIDTH = 800
MAP_HEIGHT = 600
MAP_OFFSET_X = 0
MAP_OFFSET_Y = UI_PANEL_HEIGHT

SCREEN_WIDTH = MAP_WIDTH
SCREEN_HEIGHT = UI_PANEL_HEIGHT + MAP_HEIGHT

FPS = 60

WINDOW_TITLE = "Don't mess with the stars"

UI_BACKGROUND_COLOR = (18, 18, 35)
UI_TEXT_COLOR = (240, 240, 255)