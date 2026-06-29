


class Player:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def move(self, move_x, move_y):
        if self.check_new_position(move_x, move_y):
            self.position_y = move_y
            self.position_x = move_x

    def check_new_position(self, new_position_x, new_position_y):

        return True