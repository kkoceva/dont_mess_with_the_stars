from game.game_data import Position

class Portal:
    def __init__(self, position: Position):
        self.position = position
        self.is_active = False

        self.current_animation = "portal"
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 150

    def activate(self):
        self.is_active = True

    def update_animation(self, dt, frame_count):
        if not self.is_active:
            return

        self.animation_timer += dt

        if self.animation_timer >= self.animation_speed:
            self.animation_timer -= self.animation_speed
            self.frame_index = (
                self.frame_index + 1
            ) % frame_count