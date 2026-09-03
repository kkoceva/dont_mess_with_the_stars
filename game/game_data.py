from dataclasses import dataclass

@dataclass
class PlayerResources:
    fragments:int = 0
    required_fragments: int = 3
    energy:int = 0
    required_energy:int = 100

    def add_fragment(self):
        self.fragments = min(
            self.fragments + 1,
            self.required_fragments
        )

    def add_energy(self, amount):
        self.energy = min(
            self.energy + amount,
            self.required_energy
        )

    def has_required_resources(self):
        return (
            self.fragments >= self.required_fragments
            and self.energy >= self.required_energy
        )

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