"""Main entry point for Don't Mess With the Stars."""

# pylint: disable=no-member, missing-final-newline


from game.game_controller import GameController


def main():
    game = GameController()
    game.run()


if __name__ == "__main__":
    main()