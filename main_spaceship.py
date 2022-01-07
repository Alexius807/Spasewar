import pygame


class Main_spaseship():
    def __init__(self, screen):
        """gargargarg agrggg"""

        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.right_move = False
        self.left_move = False

    def run_main(self):
        self.screen.blit(self.image, self.rect)

    def update_main(self):
        if self.right_move and self.rect.right < self.screen_rect.right:
            self.center += 1
        if self.left_move and self.rect.left > 0:
            self.center -= 1

        self.rect.centerx = self.center

    def resurrect_main(self):
        self.center = self.screen_rect.centerx

