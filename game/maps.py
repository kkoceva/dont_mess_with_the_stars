from game.settings import MAP_OFFSET_X, MAP_OFFSET_Y, TILE_SIZE


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
    """Represents and draws the game map."""

    def __init__(self, level, asset_manager):
        """Initialize the map with a level and assets."""
        self.level = level
        self.asset_manager = asset_manager

    def draw(self, screen):
        """Draw the map using textures."""
        floor_texture = self.asset_manager.get_texture("floor")
        wall_texture = self.asset_manager.get_texture("wall")
        #portal_texture = self.asset_manager.get_texture("portal")

        for row_index, row in enumerate(self.level):
            for col_index, tile in enumerate(row):
                position = (
                    col_index * TILE_SIZE,
                    MAP_OFFSET_Y + row_index * TILE_SIZE,
                )

                screen.blit(floor_texture, position)

                if tile == WALL:
                    screen.blit(wall_texture, position)
                #elif tile == PORTAL:
                    #screen.blit(portal_texture, position)

    def get_player_start_position(self):
        """Return the player start position in pixels."""
        for row_index, row in enumerate(self.level):
            for col_index, tile in enumerate(row):
                if tile == PLAYER_START:
                    return (
                        col_index * TILE_SIZE,
                        MAP_OFFSET_Y + row_index * TILE_SIZE,
                    )

        return 0, 80