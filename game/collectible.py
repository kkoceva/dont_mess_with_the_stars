from enum import Enum
from game.game_data import Position

class CollectibleType(Enum):
    STAR_CRYSTAL = 0
    ZODIAC_SIGN = 1
    CONSTELLATION_FRAGMENT = 2

class Collectible:
    def __init__(
        self, position: Position, collectible_type: CollectibleType, collectible_name, value: int):
        self.position = position
        self.collectible_type = collectible_type
        self.collectible_name = collectible_name
        self.value = value
        self.is_collected = False

    def collect(self):
        self.is_collected = True