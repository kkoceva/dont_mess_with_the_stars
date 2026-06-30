from enum import Enum

class EnemyType(Enum):
    Mercury = 0,
    Mars = 1,
    Venus = 3

class Enemy:
    def __init__(self, position, enemy_type):
        self.position = position
        self.enemy_type = enemy_type

    def set_animation(self, animation_name):
        if self.current_animation != animation_name:
            self.current_animation = animation_name
            self.frame_index = 0
            self.animation_timer = 0

