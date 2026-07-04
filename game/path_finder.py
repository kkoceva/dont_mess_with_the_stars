from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

from game.game_data import Position

class PathFinder:
    def __init__(self, level, allow_diagonal=False):
        self.level = level
        self.allow_diagonal = allow_diagonal

    def find_path(self, position, target_position):
        matrix = self._build_matrix()
        grid = Grid(matrix=matrix)

        start = grid.node(position.x, position.y)
        end = grid.node(target_position.x, target_position.y)

        diagonal_movement = (
            DiagonalMovement.only_when_no_obstacle
            if self.allow_diagonal
            else DiagonalMovement.never
        )

        finder = AStarFinder(diagonal_movement=diagonal_movement)
        path, _ = finder.find_path(start, end, grid)

        return [Position(x, y) for x, y in path]
    
    def _build_matrix(self):
        matrix = []

        for row in self.level:
            matrix_row = []

            for tile in row:
                if tile == "0":
                    matrix_row.append(0)
                else:
                    matrix_row.append(1)

            matrix.append(matrix_row)

        return matrix