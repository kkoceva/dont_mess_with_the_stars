# pylint: disable=no-member

import pygame

from game.settings import TEXTURES_DIR, TILE_SIZE


class AssetManager:
    """Loads and stores game assets."""

    def __init__(self):
        self.textures = {}

    def load_texture(self, name, file_name):
        image_path = TEXTURES_DIR / file_name
        image = pygame.image.load(image_path).convert_alpha()

        self.textures[name] = pygame.transform.scale(
            image,
            (TILE_SIZE, TILE_SIZE),
        )
    
    def load_title(self, name, file_name):
        image_path = TEXTURES_DIR / file_name
        image = pygame.image.load(image_path).convert_alpha()

        max_height = 60
        original_width = image.get_width()
        original_height = image.get_height()

        scale_ratio = max_height / original_height
        new_width = int(original_width * scale_ratio)
        new_height = int(original_height * scale_ratio)

        self.textures[name] = pygame.transform.scale(
            image,
            (new_width, new_height),
        )

    def load_all(self):
        """Load all required game assets."""
        self.load_texture("floor", "floor.png")
        self.load_texture("wall", "wall.png")
        self.load_title("title", "title.png")
        #self.load_texture("portal", "portal.png")
        print("Loaded textures:", self.textures.keys())

    def get_texture(self, name):
        return self.textures[name]