"""Main entry point for Don't Mess With the Stars."""

# pylint: disable=no-member
# pylint: disable=missing-final-newline

import pygame

from game.maps import GameMap


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (20, 20, 40)
WINDOW_TITLE = "Don't mess with the stars"


def main():
    """Run the main game loop."""
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        GameMap.draw_grid(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
        pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()