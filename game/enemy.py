from enum import Enum

class Enemy:
    def __init__(self, position, animation, path_finder, chase_range):
        self.position = position
        self.current_animation = animation
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 150
        self.path_finder = path_finder
        self.chase_range = chase_range
       
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

    def update_movement(self, player_position):
        if self.should_chase(player_position):
            self.move_towards(player_position)

    def should_chase(self, player_position):
        return self.get_distance(player_position)

    def move_towards(self, target_position):
        path = self.path_finder.find_path(
            self.position,
            target_position
        )

        if len(path) > 1:
            self.position = path[1]

    def move(self, move_x, move_y):
        if self.status.is_alive:
            self.position.x += move_x
            self.position.y += move_y

    def get_distance(self, target_position):
         distance = abs(self.position.x - target_position.x) + abs(self.position.y - target_position.y)
         return distance

    def check_target_in_range(self, target_position, range):
        return super().get_distance(target_position) <= range

    def update_stats():
        pass


class Mercury(Enemy):
    def __init__(self, position, path_finder):
        super().__init__(position, "mercury_idle", path_finder, 10)


class Mars(Enemy):
    def __init__(self, position, path_finder):
        super().__init__(position, "mars_idle", path_finder, 5)

class Venus(Enemy):
    def __init__(self, position, path_finder):
        super().__init__(position, "venus_idle", path_finder, 7)
        self.slow_range = 2

    def should_apply_effect(self, player_position):
        return self.get_distance(player_position) <= self.slow_range

    