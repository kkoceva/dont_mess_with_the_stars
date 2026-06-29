# pylint: disable=no-member

import pygame

from game.settings import (
    SCREEN_WIDTH,
    UI_BACKGROUND_COLOR,
    UI_PANEL_HEIGHT,
    UI_TEXT_COLOR,
    HUD_SEPARATOR_COLOR
)

class UIManager:
    def __init__(self, assets_manager):
        self.font = pygame.font.SysFont(None, 28)
        self.assets_manager = assets_manager

    def draw(self, screen):
        panel_rect = pygame.Rect(
            0,
            0,
            SCREEN_WIDTH,
            UI_PANEL_HEIGHT,
        )

        panel_hud_border_rect = pygame.Rect(
            0,
            0,
            SCREEN_WIDTH,
            3
        )

        pygame.draw.rect(screen, UI_BACKGROUND_COLOR, panel_rect)
        pygame.draw.rect(screen, HUD_SEPARATOR_COLOR, panel_hud_border_rect)
        title_texture = self.assets_manager.get_texture("title")
        self.draw_text(screen, "Lives: 3", 180, 28)
        self.draw_text(screen, "HP: 100", 300, 28)
        self.draw_text(screen, "Energy: 0", 440, 28)
        self.draw_text(screen, "Fragments: 0/3", 600, 28)
        self.draw_title(screen, title_texture, 10, 10)

    def draw_text(self, screen, text, x_position, y_position):
        text_surface = self.font.render(text, True, UI_TEXT_COLOR)
        screen.blit(text_surface, (x_position, y_position))

    def draw_title(self, screen, img_name, x_position, y_position):
         screen.blit(img_name, (x_position, y_position))