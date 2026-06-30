from game.game_data import Position, PlayerStatus, PlayerResources

class Player:
    def __init__(self, position):
        self.position = position
        self.status = PlayerStatus()
        self.resources = PlayerResources()
        self.current_animation = "player_idle"
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 150

    def move(self, move_x, move_y):
        if self.status.is_alive:
            self.position.x += move_x
            self.position.y += move_y

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
    