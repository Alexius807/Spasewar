import pygame
from pygame.sprite import Sprite


class Main(Sprite):

    def __init__(self, screen):
        super(Main, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    # Расположение по центру экрана
    def create_gun(self):
        self.center = self.screen_rect.centerx

    # Отрисовка игрока
    def draw_main(self):
        self.screen.blit(self.image, self.rect)

    # Обработка движения
    def update_gun(self):
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center
