import pygame
import pygame_menu

from game.settings import WHITE, LIGHT, DARK, BG

class GameMenu:
    def __init__(self, screen, start_game):
        self.screen = screen
        self.menu = pygame_menu.Menu(
            "Welcome",
            400,
            300,
            theme=pygame_menu.themes.THEME_DEFAULT
        )
        self.start_game = start_game
        self.menu.add.button('Play', start_game)
        self.menu.add.button('Quit', pygame_menu.events.EXIT)
        print([name for name in dir(pygame_menu.themes) if name.startswith("THEME_")])


    def update(self, events):
        self.menu.update(events)

    def draw(self):
        self.menu.draw(self.screen)