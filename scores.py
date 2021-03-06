import pygame.font
from main_spaceship import Main
from pygame.sprite import Group


class Scores():
    # подсчет очков
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.show_record()
        self.show_lives()

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.record_image, self.record_rect)
        self.mains.draw(self.screen)

    def image_score(self):
        # вывод текста подсчета как изображения
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_record(self):
        self.record_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.record_rect = self.record_image.get_rect()
        self.record_rect.centerx = self.screen_rect.centerx
        self.record_rect.bottomright = self.screen_rect.bottomright

    def show_lives(self):
        # жизни игрока
        self.mains = Group()
        for gun_number in range(self.stats.main_lives):
            main = Main(self.screen)
            main.rect.x = 15 + gun_number * main.rect.width
            main.rect.y = 20
            self.mains.add(main)
