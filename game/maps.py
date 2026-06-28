import pygame

class GameMap:
    BLACK = (0, 0, 0)
    white = (200, 200, 200)
    WINDOW_HEIGHT = 400
    WINDOW_WIDTH = 400

    def __init__(self, row, col):
        pass

    def create_map(self, row, col):
        pass

    @staticmethod
    def draw_grid(window_width, window_height, screen):
        """Draw the game grid."""
        white = (200, 200, 200)
        block_size = 20

        for x in range(0, window_width, block_size):
            for y in range(0, window_height, block_size):
                rect = pygame.Rect(x, y, block_size, block_size)
                pygame.draw.rect(screen, white, rect, 1)