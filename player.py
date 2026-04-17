import pygame
from sprites import GetSprites

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, SCREEN_WIDTH = 500, SCREEN_HEIGHT = 500, animation_speed = 100):
    
        # неизменяемые параметры игрока
        self.PLAYER_SIZE = 32
        self.PLAYER_SPEED = 5
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.animation_speed = animation_speed
        # задаём начальное положение игрока
        self.rect = pygame.Rect(x, y, self.PLAYER_SIZE, self.PLAYER_SIZE)
        self.speed = self.PLAYER_SPEED
        # блок с определением спрайтов
        self.Sprites =  GetSprites("assets/warrior spritesheet calciumtrice.png", 10)
        self.images = self.Sprites.get_sprite_frames(row = 0)
        self.normal_images = self.images

        #инициализируем любой кадр в качестве первого
        self.number_of_frame = 0
        self.image = self.images[self.number_of_frame]
        self.last_update = pygame.time.get_ticks()
        self.is_attacking = False
        
       


    def base_animation(self):
       # не смешиваем анимации если игрок атакует
       if self.is_attacking:
           return
       #получаем настоящий момент
       now = pygame.time.get_ticks()
       # сравниваем разность послдеднего обновления и настоящего момента со скоростью огбновления кадров
       if (now - self.last_update >= self.animation_speed) :
           #прибавляем счетчик кадров
           self.number_of_frame +=1
           # сравниваем текущий номер кадра с длиной нарезанного спрайта
           if self.number_of_frame >= len(self.images):
            # обнуляем если вышли за границы
               self.number_of_frame = 0
            # присваиваем очередной кадр
           self.image = self.images[self.number_of_frame]
           # обновляем время вставки последнего кадра
           self.last_update = now

    def attack_animation(self):
        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and not self.is_attacking:
            self.is_attacking = True
            self.number_of_frame = 0
            self.images = self.Sprites.get_sprite_frames(row = 3)
            self.image = self.images[0]
            self.last_update = now

        if self.is_attacking:
            if (now - self.last_update >= self.animation_speed):
                    self.number_of_frame += 1  
                    if self.number_of_frame >= len(self.images):
                        self.is_attacking = False
                        self.images = self.normal_images
                        self.number_of_frame = 0
                    else:
                        self.image = self.images[self.number_of_frame]
                        self.last_update = now

            
            
            


           
        

    def update_player_position(self, keys):
        #включаем анимацию сюда
        self.base_animation()
        self.attack_animation()
        #идентифицируем последнее положение игрока
        self.old_x  = self.rect.x
        self.old_y = self.rect.y
        #задаём движение покоординатно
        if keys[pygame.K_w]:
            self.rect.y -= self.speed

        if keys[pygame.K_s]:
            self.rect.y += self.speed

        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed
        #установим границы движения персонажа
        self.rect.x = max(0, min(self.rect.x, (self.SCREEN_WIDTH - self.PLAYER_SIZE)))

        self.rect.y = max(0, min(self.rect.y, (self.SCREEN_HEIGHT - self.PLAYER_SIZE)))
  

 