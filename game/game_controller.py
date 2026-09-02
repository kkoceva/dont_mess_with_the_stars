# pylint: disable=no-member
import sys
import pygame
from enum import Enum
from game.menu import GameMenu
from game.player import Player
from game.enemy import Enemy, Mercury, Venus, Mars
from game.game_data import Position
from game.maps import GameMap, LEVEL_1
from game.game_renderer import GameRenderer
from game.assets_manager import AssetManager
from game.settings import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE, MAP_OFFSET_Y, MAP_OFFSET_X, TILE_SIZE
from game.path_finder import PathFinder

class GameStateType(Enum):
    MENU = "menu",
    PLAYING = "Playing",
    WIN = "win"
    GAMEOVER = "game over"


class GameController:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(WINDOW_TITLE)
        self.assets_manager = AssetManager()
        self.game_renderer = GameRenderer(self.screen)
        self.game_map = GameMap(LEVEL_1, self.assets_manager)
       
        start_position = self.game_map.get_player_start_position()
        mercury_position = self.game_map.get_enemy_start_position()
        venus_position = self.game_map.get_enemy_start_position()
        mars_position = self.game_map.get_enemy_start_position()
        self.player = Player(start_position)
        self.path_finder = PathFinder(LEVEL_1)
        self.mercury = Mercury(mercury_position, self.path_finder)
        self.mars = Mars(mars_position, self.path_finder)
        self.venus = Venus(venus_position, self.path_finder)

        self.enemies = [
            self.mercury,
            self.venus,
            self.mars
        ]

        self.enemy_move_delay = 500
        self.last_enemy_move_time = 0

        self.clock = pygame.time.Clock()
        self.mouse = pygame.mouse.get_pos()
        self.running = True
        self.state = GameStateType.MENU
        self.game_menu = GameMenu(self.screen, self.start_game)
    
    def start_game(self):
        self.state = GameStateType.PLAYING

    def run(self):
            while self.running:
                dt = self.clock.tick(FPS)
                if self.state == GameStateType.PLAYING:
                    self.player.update_movement(dt)

                events = pygame.event.get()
                self.handle_events(events)
                if self.state == GameStateType.MENU:
                    self.game_menu.update(events)
                    self.screen.fill((18, 18, 35))
                    self.game_menu.draw()
                elif self.state == GameStateType.PLAYING:
                    self.game_renderer.update(dt, self.player)
                    self.game_renderer.update(dt, self.mercury)
                    self.game_renderer.update(dt, self.venus)
                    self.game_renderer.update(dt, self.mars)
                    self.update_game()
                    self.game_renderer.draw(self.player, self.mercury, self.venus, self.mars)

                pygame.display.flip()

            pygame.quit()
            sys.exit()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if self.state == GameStateType.PLAYING:
                if event.type == pygame.KEYDOWN:
                    self.move_player(event)
                elif event.type == pygame.KEYUP:
                    self.player.set_idle_animation()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = GameStateType.MENU

    def move_player(self, event):
        if not self.player.can_move():
            return
        
        move_x = 0
        move_y = 0

        if event.key == pygame.K_UP:
            move_y = -1
        elif event.key == pygame.K_DOWN:
            move_y = 1
        elif event.key == pygame.K_LEFT:
            move_x = -1
        elif event.key == pygame.K_RIGHT:
            move_x = 1
        else:
            return

        new_position = Position(
            self.player.position.x + move_x,
            self.player.position.y + move_y,
        )

        if self.game_map.is_tile_available(new_position):
            self.player.move(move_x, move_y)
            self.player.reset_move_timer()

    def update_game(self):
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_enemy_move_time < self.enemy_move_delay):
            return

        for enemy in self.enemies:
            enemy.update_movement(self.player.position)

        if self.venus.should_apply_effect(self.player.position):
            self.player.apply_slow(2000)

        self.last_enemy_move_time = current_time

            
    