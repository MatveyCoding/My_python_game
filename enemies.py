import pygame
from sprites import GetSprites


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_size, animation_speed = 200):
        super().__init__()
        self.enemy_size = enemy_size
        self.enemy_speed = 5
        #задаём прямоугольик врага
        #self.rect = pygame.Rect(x,y, self.enemy_size, self.enemy_size)
        self.rect = pygame.Rect(x,y, 45, 28)
        self.SCREEN_WIDTH  = 500
        self.SCREEN_HEIGHT = 500
        self.last_update = pygame.time.get_ticks()
        self.number_of_frame = 6
        self.image = None
    

           
            
class Skeleton(Enemy):
    def __init__(self, x, y, enemy_size = 45, animation_speed = 200):
        super().__init__(x, y, enemy_size, animation_speed)
        
        self.PLAYER_SIZE_HEIGHT = 52
        self.PLAYER_SIZE_WIDTH = 31
        self.Sprites =  GetSprites("assets/skeletons.png", 6, is_square = False)
        self.animation_speed = animation_speed
        self.live_status = True
        self.health = 3
        self.skeleton_images = self.Sprites.get_sprite_frames(row = 0, start_frame = 0, PLAYER_SIZE_HEIGHT = self.PLAYER_SIZE_HEIGHT, PLAYER_SIZE_WIDTH = self.PLAYER_SIZE_WIDTH  )
        self.image = self.skeleton_images[0]
        self.knockback = False
        self.knockback_velocity = 200
        self.knockback_direction = 1
    def moving_animation(self):
        if not self.skeleton_images:
            return
        #if not self.running:
                #return
        now = pygame.time.get_ticks()

        #if self.moving_right:
            #self.images = self.moving_images_right
        # else:
        # self.images = self.moving_images_left

        if (now - self.last_update >= self.animation_speed):
            self.number_of_frame -= 1
            if self.number_of_frame < 0:
                self.number_of_frame = len(self.skeleton_images)-1    
            self.image = self.skeleton_images[self.number_of_frame]
            self.last_update = now

    def update_skeleton_position(self):
        if self.knockback:
            self.rect.x += self.knockback_velocity * self.knockback_direction
            self.knockback_velocity *= 0.75
            if abs(self.knockback_velocity) < 0.5:
                self.knockback = False
        
        self.rect.x -= self.enemy_speed
        #установим границы движения персонажа
        self.rect.x = max(0, min(self.rect.x, (self.SCREEN_WIDTH - self.PLAYER_SIZE_WIDTH )))
        self.rect.y = max(0, min(self.rect.y, (self.SCREEN_HEIGHT - self.PLAYER_SIZE_HEIGHT)))
        
        self.moving_animation()





