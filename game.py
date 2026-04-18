import pygame
from player import Player
from utils import MysteryBox
from enemies import Skeleton
import random
class Game:
    #Параметры экрана
    
    def __init__(self, SCREEN_WIDTH = 500, SCREEN_HEIGHT = 500):
        #Установим размеры окна
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #Название игры
        pygame.display.set_caption("Моя игра")
        #Инициализируем время
        self.clock = pygame.time.Clock()
        
        self.box_waiting = False
        self.FPS = 30
        #выставим по умолчанию время до новой атаки
        self.new_attack_time = 0
        #дистанция атаки
        self.attack_distance = 45

        self.running = True
        self.SCREEN_WIDTH  = SCREEN_WIDTH 
        self.SCREEN_HEIGHT = SCREEN_HEIGHT 
        

        self.player = Player(x = 0,
                             y = 0, 
                             animation_speed = 100
                             )
        self.mysteryBox = MysteryBox(
                                     x = random.randint(0, SCREEN_WIDTH-24),
                                     y = random.randint(0, SCREEN_HEIGHT - 24),
                                     SCREEN_WIDTH = SCREEN_WIDTH, 
                                     SCREEN_HEIGHT = SCREEN_HEIGHT
                                    )
        self.skeleton = Skeleton( x = 450,
                                  y = random.randint(0, SCREEN_HEIGHT - 24)
                                )
        #по умолчанию добавляем коробку в группу
        self.all_sprites = pygame.sprite.Group()
        #добавляем в область живых объектов коробку и скелета
        self.all_sprites.add(self.mysteryBox)
        self.all_sprites.add(self.skeleton)

    def handle_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update_player_position(keys)
        self.skeleton.update_skeleton_position(self.player.rect.x, self.player.rect.y)



    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.player.image, self.player.rect)

        #проверили, ожидается ли новая коробка и выполнено ли условие по задержке
        if (self.box_waiting and pygame.time.get_ticks() >= self.mysteryBox.box_respawn_time):
            # поменяли координаты коробки
            self.mysteryBox.rect.topleft = (random.randint(0, self.SCREEN_WIDTH-24) , random.randint(0, self.SCREEN_HEIGHT-24))
            # записали в группу спрайтов коробку с новыми координатами
            self.all_sprites.add(self.mysteryBox)
            # выставили флаг ненужности коробки
            self.box_waiting = False
        
        # если коробка есть в группе
        if self.mysteryBox.alive():
            # рисуем коробку
            self.screen.blit(self.mysteryBox.box_image, self.mysteryBox.rect)
            # проверяем соприкосновение с ящиком
            if self.player.rect.colliderect(self.mysteryBox.rect):
                print("Коснулся!")
                self.mysteryBox.kill()
                self.box_waiting = True
                self.mysteryBox.box_respawn_time =  pygame.time.get_ticks()  + self.mysteryBox.box_respawn_delay

        ### Логика убийства скелета
        if self.skeleton.alive():  
            self.screen.blit(self.skeleton.image, self.skeleton.rect)   
            if abs(self.player.rect.x - self.skeleton.rect.x) <= self.attack_distance and self.player.is_attacking and pygame.time.get_ticks() >= self.new_attack_time:
                if self.player.rect.x < self.skeleton.rect.x:
                    if self.player.moving_right: 
                        self.skeleton.health-=1
                        #####
                        self.skeleton.knockback_direction = 1 
                        self.skeleton.knockback = True
                        self.skeleton.knockback_velocity = 50
                        
                        #####
                        print("Атака прошла!")
                        self.new_attack_time = pygame.time.get_ticks() + self.player.attack_cooldown
                        if self.skeleton.health == 0:
                            self.skeleton.kill()
                            print("Скелет повержен!")
                   
                    
                elif self.player.rect.x > self.skeleton.rect.x:
                    if not self.player.moving_right :
                        self.skeleton.health-=1
                        self.skeleton.knockback_direction = -1 
                        self.skeleton.knockback = True
                        self.skeleton.knockback_velocity = 30
                        print("Атака прошла!")
                        self.new_attack_time = pygame.time.get_ticks() + self.player.attack_cooldown
                        if self.skeleton.health == 0:
                            self.skeleton.kill()

                            print("Скелет повержен!")
                    
                
            
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            #вызываемся 60 раз в секунду
            self.clock.tick(self.FPS)
