# pylint: disable=no-member

import pygame

from game.settings import (
    SCREEN_WIDTH,
    UI_BACKGROUND_COLOR,
    UI_PANEL_HEIGHT,
    UI_TEXT_COLOR,
    HUD_SEPARATOR_COLOR,
)

class UIManager:
    def __init__(self, assets_manager):
        self.font = pygame.font.SysFont(None, 28)
        self.assets_manager = assets_manager

    def draw(self, screen, player):
        panel_rect = pygame.Rect(
            0,
            0,
            SCREEN_WIDTH,
            UI_PANEL_HEIGHT
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
        menu_button = self.assets_manager.get_texture("menu_button")
        self.draw_text(screen, f"Lives: {player.status.lives}", 180, 28)
        self.draw_text(screen, f"HP: {player.status.hp}", 300, 28)
        self.draw_text(screen, f"Energy: {player.resources.energy}", 440, 28)
        self.draw_text(screen, f"Fragments: {player.resources.fragments}/{player.resources.required_fragments}", 600, 28)
        self.draw_title(screen, title_texture, 10, 10)
        self.draw_title(screen, menu_button, 860, 10)

    def draw_text(self, screen, text, x_position, y_position):
        text_surface = self.font.render(text, True, UI_TEXT_COLOR)
        screen.blit(text_surface, (x_position, y_position))

    def draw_title(self, screen, img_name, x_position, y_position):
         screen.blit(img_name, (x_position, y_position))

    def draw_win_screen(self, screen):
        screen.fill((18, 18, 35))

        font = pygame.font.Font(None, 80)

        text = font.render(
            "YOU WIN!",
            True,
            (255, 215, 80),
        )

        text_rectangle = text.get_rect(
            center=screen.get_rect().center
        )

        screen.blit(text, text_rectangle)

    def draw_lost_screen(self, screen):
        screen.fill((18, 18, 35))

        font = pygame.font.Font(None, 80)

        text = font.render(
            "YOU Lose!",
            True,
            (255, 215, 80),
        )

        text_rectangle = text.get_rect(
            center=screen.get_rect().center
        )

        screen.blit(text, text_rectangle)