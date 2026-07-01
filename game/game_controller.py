# pylint: disable=no-member

import pygame


from game.player import Player
from game.enemy import Enemy
from game.game_data import Position
from game.game_renderer import GameRenderer
from game.maps import GameMap, LEVEL_1
from game.assets_manager import AssetManager
from game.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE, MAP_OFFSET_Y, MAP_OFFSET_X, TILE_SIZE

class GameController:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.assets_manager = AssetManager()
        self.game_renderer = GameRenderer(self.screen)
        self.game_map = GameMap(LEVEL_1, self.assets_manager)
        start_position = self.game_map.get_player_start_position()
        self.player = Player(start_position)
        self.mercury = Enemy(start_position, 0)
        self.mars = Enemy(start_position, 1)
        self.venus = Enemy(start_position, 2)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
            while self.running:
                dt = self.clock.tick(FPS)
                self.handle_events()
                self.game_renderer.update(dt, self.player)
                self.game_renderer.draw(self.player)
                self.clock.tick(FPS)

            pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.move_player(event)
            elif event.type == pygame.KEYUP:
                self.player.set_animation("player_idle")

    def move_player(self, event):
        move_x = 0
        move_y = 0

        if event.key == pygame.K_UP:
            move_y = -1
            self.player.set_animation("player_walk_up")
        elif event.key == pygame.K_DOWN:
            move_y = 1
            self.player.set_animation("player_walk_down")
        elif event.key == pygame.K_LEFT:
            move_x = -1
            self.player.set_animation("player_walk_left")
        elif event.key == pygame.K_RIGHT:
            move_x = 1
            self.player.set_animation("player_walk_right")
        else:
            return

        new_position = Position(
            self.player.position.x + move_x,
            self.player.position.y + move_y,
        )

        if self.game_map.is_moving(new_position):
            self.player.move(move_x, move_y)
    