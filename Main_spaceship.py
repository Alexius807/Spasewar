import pygame


class Main_spaseship():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Pictures/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def run_main(self):
        self.screen.blit(self.image, self.rect)