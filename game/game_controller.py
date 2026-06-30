# pylint: disable=no-member

import pygame

from game.game_renderer import GameRenderer
from game.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE, MAP_OFFSET_Y, MAP_OFFSET_X, TILE_SIZE

class GameController:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)

        self.game_renderer = GameRenderer(self.screen)

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
            while self.running:
                dt = self.clock.tick(FPS)
                self.handle_events()
                self.game_renderer.update(dt)
                self.game_renderer.draw()
                self.clock.tick(FPS)

            pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.game_renderer.move_player(event)
            elif event.type == pygame.KEYUP:
                self.game_renderer.player.set_animation("player_idle")
    