import pygame
from sprites import GetSprites
import random
class MysteryBox(pygame.sprite.Sprite):

    def __init__(self, x, y, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__() 
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.box_image_original = pygame.image.load("assets/crate_box.png").convert_alpha()
        
        self.box_image = pygame.transform.smoothscale(self.box_image_original, (24,24))

        self.rect = self.box_image.get_rect(topleft = (x,y))

