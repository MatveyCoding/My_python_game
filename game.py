import pygame
from player import Player
from utils import MysteryBox
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

        self.FPS = 60

        self.running = True
        
        

        self.player = Player(x = 0,
                             y = 0, 
                             SCREEN_WIDTH = SCREEN_WIDTH, 
                             SCREEN_HEIGHT = SCREEN_HEIGHT,
                             animation_speed = 100
                             )
        self.mysteryBox = MysteryBox(
                                     x = random.randint(0, SCREEN_WIDTH-24),
                                     y = random.randint(0, SCREEN_HEIGHT - 24),
                                     SCREEN_WIDTH = SCREEN_WIDTH, 
                                     SCREEN_HEIGHT = SCREEN_HEIGHT
                                    )
        
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.mysteryBox)
    def handle_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update_player_position(keys)


    def draw(self):
        self.screen.fill((0,0,0))
        #pygame.draw.rect(self.screen, self.player.player_visual, self.player.rect)
        self.screen.blit(self.player.image, self.player.rect)
        
        if self.mysteryBox.alive():
            self.screen.blit(self.mysteryBox.box_image, self.mysteryBox.rect)

            if self.player.rect.colliderect(self.mysteryBox.rect):
                print("Коснулся!")
                self.mysteryBox.kill()
            
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            #вызываемся 60 раз в секунду
            self.clock.tick(self.FPS)
