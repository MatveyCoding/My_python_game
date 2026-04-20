import pygame


class GetSprites:
      def __init__(self, sprite_path, num_frames, sizе = 32, is_square = True):
            self.sprite_path = sprite_path
            self.num_frames = num_frames
            self.PLAYER_SIZE = sizе
            self.is_square = is_square

      def get_sprite_frames(self, row = 0, start_frame = 0, SIZE_WIDTH=0, SIZE_HEIGHT=0 ):
            self.sprite_images =  pygame.image.load(self.sprite_path).convert_alpha()
            frames = []
            for frame_count in range(start_frame, self.num_frames):
                  if self.is_square == False:
                        frame_rect = pygame.Rect(frame_count * SIZE_WIDTH  , row * SIZE_HEIGHT, SIZE_WIDTH, SIZE_HEIGHT)
                  else:
                        frame_rect = pygame.Rect(frame_count * self.PLAYER_SIZE, row * self.PLAYER_SIZE, self.PLAYER_SIZE, self.PLAYER_SIZE)

                  frame = self.sprite_images.subsurface(frame_rect)
                  frames.append(frame)
            return frames