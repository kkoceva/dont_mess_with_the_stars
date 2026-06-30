import pygame

from game.player import Player
from game.enemy import Enemy
from game.game_data import Position
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
        start_position = self.game_map.get_player_start_position()
        self.player = Player(start_position)
        self.mercury = Enemy(start_position, 0)
        self.mars = Enemy(start_position, 1)
        self.venus = Enemy(start_position, 2)
        self.screen = screen

    def draw(self):
        self.game_map.draw(self.screen)
        self.draw_player()
        self.ui_manager.draw(self.screen)
      
        pygame.display.flip()

    def draw_player(self):
        frames = self.assets_manager.get_animation(self.player.current_animation)
        player_frame = frames[self.player.frame_index]

        x = MAP_OFFSET_X + self.player.position.x * TILE_SIZE
        y = MAP_OFFSET_Y + self.player.position.y * TILE_SIZE

        self.screen.blit(player_frame, (x, y))

    def update(self, dt):
        frames = self.assets_manager.get_animation(self.player.current_animation)
        self.player.update_animation(dt, len(frames))

        print(self.player.current_animation, self.player.frame_index)
    
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
