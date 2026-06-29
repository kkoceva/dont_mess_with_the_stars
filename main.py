"""Main entry point for Don't Mess With the Stars."""

# pylint: disable=no-member, missing-final-newline

import pygame

from game.game_controller import GameController


def main():

    game = GameController()
    game.run()
    pygame.init()


if __name__ == "__main__":
    main()