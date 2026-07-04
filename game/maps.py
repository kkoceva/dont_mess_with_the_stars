import random

from game.settings import MAP_OFFSET_Y, TILE_SIZE
from game.game_data import Position

FLOOR = "1"
WALL = "0"
PLAYER_START = "P"
PORTAL = "O"
ENEMY = "E"
COLLECTIBLE = "C"


LEVEL_1 = [
    "00000000000000000000",
    "01111111111111111110",
    "01100000111111111110",
    "01111110111111111110",
    "01111110111100001110",
    "01111110111111111110",
    "01100000000000111110",
    "01111111111111111110",
    "01111100001111111110",
    "01111111110111111110",
    "01111111110111000010",
    "01111111111111111110",
    "01111000000111111110",
    "01111111111111111110",
    "00000000000000000000",
]

class GameMap:
    def __init__(self, level, asset_manager):
        self.level = level
        self.asset_manager = asset_manager
        self.occupied_positions = []

    def draw(self, screen):
        floor_texture = self.asset_manager.get_texture("floor")
        wall_texture = self.asset_manager.get_texture("wall")
        for row_index, row in enumerate(self.level):
            for col_index, tile in enumerate(row):
                position = (
                    col_index * TILE_SIZE,
                    MAP_OFFSET_Y + row_index * TILE_SIZE,
                )
                screen.blit(floor_texture, position)
                if tile == WALL:
                    screen.blit(wall_texture, position)

    def get_player_start_position(self):
        # for row_index, row in enumerate(self.level):
        #     for col_index, tile in enumerate(row):
        #         if tile == PLAYER_START:
        #             return Position(col_index, row_index)

        return Position(1, 1)
    
    def get_enemy_start_position(self):
        if occupied_positions is None:
            occupied_positions = []

        available_positions = []

        for y, row in enumerate(self.level):
            for x, _ in enumerate(row):
                position = Position(x, y)

                if self.is_tile_available(position, occupied_positions):
                    available_positions.append(position)

        if not available_positions:
            raise ValueError("No available position for enemy.")

        return random.choice(available_positions)


    def is_tile_available(self, position):
        if position.y < 0 or position.y >= len(self.level):
            return False

        if position.x < 0 or position.x >= len(self.level[0]):
            return False

        return self.level[position.y][position.x] != WALL
    
    def is_occupied(self, position):
        pass