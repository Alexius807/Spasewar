import pygame


class Ammo(pygame.sprite.Sprite):
    def __init__(self, screen, main):
        super(Ammo, self).__init__()
        self.screen = screen
        self.y = float(self.rect.y)
        self.speed = 5
        self.rect.centerx = main.rect.centerx
        self.rect.top = main.rect.top
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.color = 255, 86, 34

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)