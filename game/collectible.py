from enum import Enum

class CollectibleType(Enum):
    STAR_CRYSTAL = 0
    ZODIAC_SIGN = 1
    CONSTELLATION_FRAGMENT = 2

class Collectible:
    def __init__(self, position, collectible_type, value = 1):
        self.position = position
        self.collectible_type = collectible_type
        self.value = value