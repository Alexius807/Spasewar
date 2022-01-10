import os
import sys
import pygame.font

import pygame, moving

from main_spaceship import Main
from pygame.sprite import Group
from game_info import Game_info
from scores import Scores

size = width, height = 700, 800


# def load_image(name, colorkey=None):
#     fullname = os.path.join('images', name)
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     return image
#
#
# def terminate():
#     pygame.quit()
#     sys.exit()
#
#
# def start_screen():
#     screen = pygame.display.set_mode(size)
#     intro_text = ["ЗАСТАВКА", "",
#                   "Правила игры",
#                   "Если в правилах несколько строк,",
#                   "приходится выводить их построчно"]
#
#     fon = pygame.transform.scale(load_image('fon.jpg'), (width, height))
#     screen.blit(fon, (0, 0))
#     font = pygame.font.Font(None, 30)
#     text_coord = 50
#     for line in intro_text:
#         string_rendered = font.render(str(line), True, pygame.Color('white'), (0, 0, 0))
#         intro_rect = string_rendered.get_rect()
#         text_coord += 10
#         intro_rect.top = text_coord
#         intro_rect.x = 10
#         text_coord += intro_rect.height
#         screen.blit(string_rendered, intro_rect)
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 terminate()
#             elif event.type == pygame.KEYDOWN or \
#                     event.type == pygame.MOUSEBUTTONDOWN:
#                 run()
#         pygame.display.flip()


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Spase War")
    bg_color = (0, 0, 0)
    main = Main(screen)
    ammos = Group()
    enemies = Group()
    moving.start_attack(screen, enemies)
    stats = Game_info()
    sc = Scores(screen, stats)

    while True:
        moving.events(screen, main, ammos)
        if stats.run_game:
            main.update_main()
            moving.update(bg_color, screen, stats, sc, main, enemies, ammos)
            moving.update_ammos(screen, stats, sc, enemies, ammos)
            moving.update_enemies(stats, screen, sc, main, enemies, ammos)


start_screen()
