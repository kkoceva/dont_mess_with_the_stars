from enum import Enum

class Enemy:
    def __init__(self, position, animation):
        self.position = position
        self.current_animation = animation
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 150
       

    def set_animation(self, animation_name):
        if self.current_animation != animation_name:
            self.current_animation = animation_name
            self.frame_index = 0
            self.animation_timer = 0

    def update_animation(self, dt, frames_count):
        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % frames_count

    def move(self, move_x, move_y):
        if self.status.is_alive:
            self.position.x += move_x
            self.position.y += move_y

    def update_stats():
        pass


class Mercury(Enemy):
    def __init__(self, position):
        super().__init__(position, "mercury_idle")

    def move(self, move_x, move_y):
        super().move(self, move_x, move_y)


class Mars(Enemy):
    def __init__(self, position):
        super().__init__(position, "mars_idle")

    def move(self, move_x, move_y):
        super().move(self, move_x, move_y)


class Venus(Enemy):
    def __init__(self, position):
        super().__init__(position, "venus_idle")

    def move(self, move_x, move_y):
        super().move(self, move_x, move_y)
        
