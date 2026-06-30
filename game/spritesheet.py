import pygame


class SpriteSheet:
    def __init__(self, file_path):
        self.sheet = pygame.image.load(file_path).convert_alpha()

    def get_frame(self, col, row, frame_width, frame_height, target_size=None):
        frame = pygame.Surface((frame_width, frame_height), pygame.SRCALPHA).convert_alpha()

        frame.blit(
            self.sheet,
            (0, 0),
            pygame.Rect(
                col * frame_width,
                row * frame_height,
                frame_width,
                frame_height,
            ),
        )

        if target_size is not None:
            frame = pygame.transform.scale(frame, target_size)

        return frame

    def get_row_frames(self, row, frame_count, frame_width, frame_height, target_size=None):
        return [
            self.get_frame(col, row, frame_width, frame_height, target_size)
            for col in range(frame_count)
        ]