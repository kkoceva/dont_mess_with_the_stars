"""Main entry point for Don't Mess With the Stars."""

# pylint: disable=no-member, missing-final-newline

import pygame

from game.assets_manager import AssetManager
from game.maps import GameMap, LEVEL_1
from game.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE


def main():
    """Run the main game loop."""
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    assets_manager = AssetManager()
    assets_manager.load_all()

    game_map = GameMap(LEVEL_1, assets_manager)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_map.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()