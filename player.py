import pygame
from sprites import GetSprites

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, animation_speed = 100):
    
        # неизменяемые параметры игрока
        self.PLAYER_SIZE = 32
        self.PLAYER_SPEED = 5
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800
        self.animation_speed = animation_speed
        self.health = 5
        # задаём прямоугольник игрока
        self.rect = pygame.Rect(x, y, self.PLAYER_SIZE, self.PLAYER_SIZE)

        # блок с определением спрайтов
        self.Sprites =  GetSprites("assets/warrior spritesheet calciumtrice.png", 10, self.PLAYER_SIZE)

        ####СТАТИЧНОЕ ПОЛОЖЕНИЕ
        #Определяем базовое статичное положение игрока(Правое)
        self.images = self.Sprites.get_sprite_frames(row = 0)
        self.normal_images = self.images
        self.moving_right = True
        #Определяем движение базовое статичное положение игрока(левое)
        self.normal_images_moving_left = [pygame.transform.flip(image, True, False)  for image in self.normal_images]

        ###БЕГ
        # Определяем анимацию бега вправо
        self.moving_images_right = self.Sprites.get_sprite_frames(row = 7)
        # Определяем анимацию бега влево
        self.moving_images_left = [pygame.transform.flip(image, True, False) for image in self.moving_images_right]
        # Изначально игрок не бежит
        self.running = False

        

        ###АТАКА
        self.attack_images_right = self.Sprites.get_sprite_frames(row = 3)
        self.attack_images_left = [pygame.transform.flip(image, True, False)  for image in self.attack_images_right]
        self.attack_cooldown = 1500

        #инициализируем любой кадр в качестве первого
        self.number_of_frame = 0
        self.image = self.images[self.number_of_frame]
        self.last_update = pygame.time.get_ticks()
        self.is_attacking = False
        
       


    def base_animation(self):
       # не смешиваем анимации если игрок атакует
       if self.is_attacking or self.running:
            return
       #загружаем спрайты в соответствии с направлением движения
       if self.moving_right:
           self.images = self.normal_images
       else:
           self.images = self.normal_images_moving_left

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
            if self.moving_right:
                self.images = self.attack_images_right
            else:
                self.images = self.attack_images_left
            self.image = self.images[0]
            self.last_update = now

        if self.is_attacking:
            if (now - self.last_update >= self.animation_speed-50):
                    self.number_of_frame += 1  
                    if self.number_of_frame >= len(self.images):
                        self.is_attacking = False
                        self.images = self.normal_images
                        self.number_of_frame = 0
                    else:
                        self.image = self.images[self.number_of_frame]
                        self.last_update = now

    def moving_animation(self):
        if self.is_attacking:
           return

        if not self.running:
            return
        
        now = pygame.time.get_ticks()

        if self.moving_right:
            self.images = self.moving_images_right
        else:
            self.images = self.moving_images_left

        
        if (now - self.last_update >= self.animation_speed-180):
            self.number_of_frame += 1
            if self.number_of_frame >= len(self.images):
                self.number_of_frame = 0     
            self.image = self.images[self.number_of_frame]
            self.last_update = now


    def update_player_position(self, keys):
        if keys[pygame.K_a]:
            self.moving_right = False
        if keys[pygame.K_d]:
            self.moving_right = True
        self.running = keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]
        #идентифицируем последнее положение игрока
        self.old_x  = self.rect.x
        self.old_y = self.rect.y
        #задаём движение покоординатно
        if keys[pygame.K_w]:
            self.rect.y -= self.PLAYER_SPEED

        if keys[pygame.K_s]:
            self.rect.y += self.PLAYER_SPEED

        if keys[pygame.K_a]:
            self.rect.x -= self.PLAYER_SPEED

        if keys[pygame.K_d]:
            self.rect.x += self.PLAYER_SPEED
        #установим границы движения персонажа
        self.rect.x = max(0, min(self.rect.x, (self.SCREEN_WIDTH - self.PLAYER_SIZE)))

        self.rect.y = max(0, min(self.rect.y, (self.SCREEN_HEIGHT-80 - self.PLAYER_SIZE)))

        self.attack_animation()
        # Потом бег (если не атакует)
        self.moving_animation()
        # Потом простой (если не атакует и не бежит)
        self.base_animation()

 