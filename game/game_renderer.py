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

    def draw(self, player, collectibles, *enemies):
        self.game_map.draw(self.screen)
        self.draw_collectibles(collectibles)
        self.draw_game_object(player)
        for enemy in enemies:
            self.draw_game_object(enemy)

        #for collectible in collectibles:
         #   self.draw_game_object(collectible)
      
        self.ui_manager.draw(self.screen, player)

    def draw_game_object(self, game_object):
        frames = self.assets_manager.get_animation(game_object.current_animation)
        game_object_frame = frames[game_object.frame_index]

        x = MAP_OFFSET_X + game_object.position.x * TILE_SIZE
        y = MAP_OFFSET_Y + game_object.position.y * TILE_SIZE

        self.screen.blit(game_object_frame, (x, y))
   
    def update(self, dt, player):
        frames = self.assets_manager.get_animation(player.current_animation)
        player.update_animation(dt, len(frames))

    def draw_collectibles(self, collectibles):
        for collectible in collectibles:
            texture = self.assets_manager.get_texture(
                collectible.texture_name
            )

            x_position = (
                MAP_OFFSET_X
                + collectible.position.x * TILE_SIZE
            )
            y_position = (
                MAP_OFFSET_Y
                + collectible.position.y * TILE_SIZE
            )

            self.screen.blit(
                texture,
                (x_position, y_position),
            )