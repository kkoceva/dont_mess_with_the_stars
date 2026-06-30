# pylint: disable=no-member

import pygame

from game.spritesheet import SpriteSheet
from game.settings import TEXTURES_DIR, TILE_SIZE


class AssetManager:
    """Loads and stores game assets."""

    def __init__(self):
        self.textures = {}
        self.animations = {}

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
        self.load_texture("floor", "floor.png")
        self.load_texture("wall", "wall.png")
        self.load_title("title", "title.png")
        self.load_player_animations()
        ##self.load_texture("player", "player.png")
        #self.load_texture("portal", "portal.png")
        print("Loaded textures:", self.textures.keys())

    def get_texture(self, name):
        return self.textures[name]
    
    def load_player_animations(self):
        sheet = SpriteSheet(TEXTURES_DIR / "player_spritesheet.png")

        frame_width = 64
        frame_height = 64
        frame_count = 4

        target_size = (TILE_SIZE, TILE_SIZE)

        self.animations["player_idle"] = sheet.get_row_frames(
            row=0,
            frame_count=frame_count,
            frame_width=frame_width,
            frame_height=frame_height,
            target_size=target_size,
        )

        self.animations["player_walk_down"] = sheet.get_row_frames(
            1, frame_count, frame_width, frame_height, target_size
        )

        self.animations["player_walk_left"] = sheet.get_row_frames(
            2, frame_count, frame_width, frame_height, target_size
        )

        self.animations["player_walk_right"] = sheet.get_row_frames(
            3, frame_count, frame_width, frame_height, target_size
        )

        self.animations["player_walk_up"] = sheet.get_row_frames(
            4, frame_count, frame_width, frame_height, target_size
        )

        self.animations["player_stunned"] = sheet.get_row_frames(
            5, frame_count, frame_width, frame_height, target_size
        )

    def get_animation(self, name):
        return self.animations[name]