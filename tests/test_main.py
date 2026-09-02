import unittest
from unittest.mock import patch

from main import main


class MainTests(unittest.TestCase):

    @patch("main.GameController")
    def test_main_starts_game(self, mock_game_controller):
        mock_game = mock_game_controller.return_value

        main()

        mock_game_controller.assert_called_once_with()
        mock_game.run.assert_called_once_with()

if __name__ == "__main__":
    unittest.main()