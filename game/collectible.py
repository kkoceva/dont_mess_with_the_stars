from enum import Enum
from game.game_data import Position

class CollectibleType(Enum):
    STAR_CRYSTAL = 0
    ZODIAC_SIGN = 1
    CONSTELLATION_FRAGMENT = 2

class Collectible:
    def __init__(
        self,
        position,
        collectible_type,
        texture_name,
        value,
    ):
        self.position = position
        self.collectible_type = collectible_type
        self.texture_name = texture_name
        self.value = value

    def collect(self):
        self.is_collected = True