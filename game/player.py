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
        self.move_interval = 150
        self.slow_timer = 0
        self.move_timer = 150

    def move(self, move_x, move_y):
        if self.status.is_alive:
            self.position.x += move_x
            self.position.y += move_y
            self.set_move_animation(move_x, move_y)

    def apply_slow(self, duration):
        self.move_interval = 300
        self.slow_timer = duration

    def update_movement(self, dt):
        self.move_timer += dt

        if self.slow_timer > 0:
            self.slow_timer -= dt

        if self.slow_timer <= 0:
            self.slow_timer = 0
            self.move_interval = 150

    def can_move(self):
        return self.move_timer >= self.move_interval

    def reset_move_timer(self):
        self.move_timer = 0

    def set_move_animation(self, move_x, move_y):
        if move_y < 0:
            self.set_animation("player_walk_up")
        elif move_y > 0:
            self.set_animation("player_walk_down")
        elif move_x < 0:
            self.set_animation("player_walk_left")
        elif move_x > 0:
            self.set_animation("player_walk_right")

    def set_idle_animation(self):
        self.set_animation("player_idle")

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

    