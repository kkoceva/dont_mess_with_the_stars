# pylint: disable=no-member

import pygame

from game.assets_manager import AssetManager
from game.ui_manager import UIManager
from game.maps import GameMap, LEVEL_1
from game.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE, MAP_OFFSET_Y

class GameController:

    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.assets_manager = AssetManager()
        self.assets_manager.load_all()

        self.ui_manager = UIManager(self.assets_manager)
        self.game_map = GameMap(LEVEL_1, self.assets_manager)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
            """Run the main game loop."""
            while self.running:
                self.handle_events()
                self.draw()
                self.clock.tick(FPS)

            pygame.quit()

    def handle_events(self):
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        """Draw all game elements."""
        self.game_map.draw(self.screen)
        self.ui_manager.draw(self.screen)

        pygame.display.flip()