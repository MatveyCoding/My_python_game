import pygame


class GetSprites:
      def __init__(self, sprite_path, num_frames):
            self.sprite_path = sprite_path
            self.num_frames = num_frames
            self.PLAYER_SIZE = 32
      def get_sprite_frames(self, row = 0):
            self.sprite_images =  pygame.image.load(self.sprite_path).convert_alpha()
            frames = []
            for frame_count in range(self.num_frames):
                  frame_rect = pygame.Rect(frame_count * self.PLAYER_SIZE , row * self.PLAYER_SIZE, self.PLAYER_SIZE, self.PLAYER_SIZE)
                  frame = self.sprite_images.subsurface(frame_rect)
                  frames.append(frame)
            return frames