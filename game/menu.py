import pygame
import pygame_menu

from game.settings import WHITE, LIGHT, DARK, BG

class GameMenu:
    def __init__(self, screen, start_game):
        self.screen = screen
        custom_theme = pygame_menu.themes.THEME_DARK.copy()
        custom_theme.background_color = (18, 18, 35)
        custom_theme.title_background_color = (35, 35, 70)
        custom_theme.title_font_color = (255, 255, 255)
        custom_theme.widget_font_color = (255, 255, 255)
        custom_theme.selection_color = (255, 220, 120)
        custom_theme.widget_font_size = 32
        custom_theme.title_font_size = 44

        self.menu = pygame_menu.Menu(
            "Welcome",
            400,
            300,
            theme=custom_theme
        )
        self.start_game = start_game
        self.menu.add.button('Play', start_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        print([name for name in dir(pygame_menu.themes) if name.startswith("THEME_")])

    def update(self, events):
        self.menu.update(events)

    def draw(self):
        self.menu.draw(self.screen)