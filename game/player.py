from game.game_data import Position, PlayerStatus, PlayerResources

class Player:
    def __init__(self, position):
        self.position = position
        self.status = PlayerStatus()
        self.resources = PlayerResources()

    def move(self, move_x, move_y):
        if self.status.is_alive:
            self.position.x += move_x
            self.position.y += move_y
    