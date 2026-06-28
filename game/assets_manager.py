"""Asset loading and management."""

# pylint: disable=no-member

import pygame

from game.settings import TEXTURES_DIR, TILE_SIZE


class AssetManager:
    """Loads and stores game assets."""

    def __init__(self):
        """Initialize the asset manager."""
        self.textures = {}

    def load_texture(self, name, file_name):
        """Load, scale and store a texture."""
        image_path = TEXTURES_DIR / file_name
        image = pygame.image.load(image_path).convert_alpha()

        self.textures[name] = pygame.transform.scale(
            image,
            (TILE_SIZE, TILE_SIZE),
        )

    def load_all(self):
        """Load all required game assets."""
        self.load_texture("floor", "floor.png")
        self.load_texture("wall", "wall.png")
        #self.load_texture("portal", "portal.png")

    def get_texture(self, name):
        """Return a texture by name."""
        return self.textures[name]