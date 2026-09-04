from game.game_data import Position

class Portal:
    def __init__(self, position: Position):
        self.position = position
        self.is_active = False
        self.current_animation = "portal"
        self.frame_index = 0

    def activate(self):
        self.is_active = True