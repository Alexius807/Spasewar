import pygame


# Класс для снарядов игрока
class Ammo(pygame.sprite.Sprite):

    def __init__(self, screen, main):
        super(Ammo, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = 139, 195, 74
        self.speed = 5
        self.rect.centerx = main.rect.centerx
        self.rect.top = main.rect.top
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw_ammo(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
