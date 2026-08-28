from enum import Enum

class Enemy:
    def __init__(self, position):
        self.position = position

    def set_animation(self, animation_name):
        if self.current_animation != animation_name:
            self.current_animation = animation_name
            self.frame_index = 0
            self.animation_timer = 0

    def move(self, move_x, move_y, speed):
        if self.status.is_alive:
            self.position.x += move_x
            self.position.y += move_y

    def update_stats():
        pass


class Mercury(Enemy):
    def __init__(self, position):
        super().__init__(position)

    def move(self, move_x, move_y):
        super().move(self, move_x, move_y)


class Mars(Enemy):
    def __init__(self, position):
        super().__init__(position)

    def move(self, move_x, move_y):
        super().move(self, move_x, move_y)


class Venus(Enemy):
    def __init__(self, position):
        super().__init__(position)

    def move(self, move_x, move_y):
        super().move(self, move_x, move_y)
        
