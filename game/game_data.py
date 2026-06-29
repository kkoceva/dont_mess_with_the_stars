from dataclasses import dataclass

@dataclass
class PlayerResources:
    fragments:int = 0
    requiered_fragments:int = 3
    energy:int = 0
    required_energy:int = 100

@dataclass
class PlayerStatus:
    hp:int = 100
    max_hp:int = 100
    lives:int = 3
    max_lives:int = 3
    is_alive:bool = True

@dataclass
class Position:
    x:int = 0
    y:int = 0