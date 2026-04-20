import pygame
from sprites import GetSprites
import random
class MysteryBox(pygame.sprite.Sprite):

    def __init__(self, x, y, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().__init__() 
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        #время респавна коробки после её сбора
        self.box_respawn_time = 0
        #задержка появления коробки
        self.box_respawn_delay = 3000
        self.box_image_original = pygame.image.load("assets/crate_box.png").convert_alpha()
        
        self.box_image = pygame.transform.smoothscale(self.box_image_original, (24,24))

        self.rect = self.box_image.get_rect(topleft = (x,y))

class HealthBar(pygame.sprite.Sprite):
    def __init__(self,SCREEN_WIDTH):
        super().__init__()
        self.current_health = 5
        self.health_bar_width = 208
        self.self_bar_height = 32
        self.rect = pygame.Rect(SCREEN_WIDTH-self.health_bar_width, 735, self.health_bar_width, self.self_bar_height)
        self.Sprites =  GetSprites("assets/health_fixed.png", 1, is_square= False) #208 x 43 - одна строчка     
        self.curent_image_health_bar = 0
        self.health_bar_images = self.Sprites.get_sprite_frames(row = 0, start_frame = 0, SIZE_WIDTH = 208, SIZE_HEIGHT= 34)
        self.health_bar_image = self.health_bar_images[self.curent_image_health_bar]
       
        
        
        
        
    def change_health_bar(self):
        self.curent_image_health_bar+=1
        self.health_bar_images = self.Sprites.get_sprite_frames(row = self.curent_image_health_bar, start_frame = 0, SIZE_WIDTH = 208, SIZE_HEIGHT= 40)
        self.health_bar_image = self.health_bar_images[0]
        return self.health_bar_image

        

    

