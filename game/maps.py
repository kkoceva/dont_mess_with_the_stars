from game.settings import MAP_OFFSET_Y, TILE_SIZE
from game.game_data import Position
from game.player import Player

FLOOR = "."
WALL = "#"
PLAYER_START = "P"
PORTAL = "O"


LEVEL_1 = [
    "####################",
    "#P.................#",
    "#..#####...........#",
    "#......#...........#",
    "#......#....####...#",
    "#......#...........#",
    "#..###########.....#",
    "#..................#",
    "#.....####.........#",
    "#.........#........#",
    "#.........#...####.#",
    "#..................#",
    "#....######........#",
    "#..................#",
    "####################",
]

class GameMap:
    def __init__(self, level, asset_manager):
        self.level = level
        self.asset_manager = asset_manager

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
        for row_index, row in enumerate(self.level):
            for col_index, tile in enumerate(row):
                if tile == PLAYER_START:
                    return Position(col_index, row_index)

        return Position(0, 0)
    
    def draw_player(self, screen, player_texture):
        tile_size_x, tile_size_y = self.get_player_start_position()
        x = self.player.position.x * tile_size_x
        y = self.player.position.y * tile_size_y
        screen.blit(player_texture, (x, y))

    def is_moving(self, position):
        if position.y < 0 or position.y >= len(self.level):
            return False

        if position.x < 0 or position.x >= len(self.level[0]):
            return False

        return self.level[position.y][position.x] != WALL