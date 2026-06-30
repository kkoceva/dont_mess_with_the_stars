from enum import Enum

class CollectibleType(Enum):
    StarCrystal = 0,
    ZodiacSign = 1,
    ConstellationFragment = 3

class Collectible:
    def __init__(self, position):
        self.position = position