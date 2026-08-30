import pygame

from game.assets_manager import AssetManager
from game.ui_manager import UIManager
from game.maps import GameMap, LEVEL_1
from game.settings import MAP_OFFSET_Y, MAP_OFFSET_X, TILE_SIZE

class GameRenderer:
    def __init__(self, screen):
        self.assets_manager = AssetManager()
        self.assets_manager.load_all()
        self.ui_manager = UIManager(self.assets_manager)
        self.game_map = GameMap(LEVEL_1, self.assets_manager)
        self.screen = screen

    def draw(self, player, mercury):
        self.game_map.draw(self.screen)
        self.draw_player(player)
        self.draw_enemy(mercury)
      
        self.ui_manager.draw(self.screen)
      
        pygame.display.flip()

    def draw_player(self, player):
        frames = self.assets_manager.get_animation(player.current_animation)
        player_frame = frames[player.frame_index]

        x = MAP_OFFSET_X + player.position.x * TILE_SIZE
        y = MAP_OFFSET_Y + player.position.y * TILE_SIZE

        self.screen.blit(player_frame, (x, y))

    def draw_enemy(self, enemy):
        frames = self.assets_manager.get_animation(enemy.current_animation)
        enemy_frame = frames[enemy.frame_index]

        x = MAP_OFFSET_X + enemy.position.x * TILE_SIZE
        y = MAP_OFFSET_Y + enemy.position.y * TILE_SIZE

        self.screen.blit(enemy_frame, (x, y))

    def update(self, dt, player):
        frames = self.assets_manager.get_animation(player.current_animation)
        player.update_animation(dt, len(frames))

        print(player.current_animation, player.frame_index)
    
    
