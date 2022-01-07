import pygame, moving
from main_spaceship import Main_spaseship
from pygame.sprite import Group
from game_info import Game_info
import time


def start():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Spase war')
    bg_color = (0, 0, 0)
    main = Main_spaseship(screen)
    ammos = Group
    enemies = Group
    moving.start_attack(screen, enemies)
    game_info = Game_info

    while True:
        moving.check_events(screen, main, ammos)
        if game_info.start:
            main.update_main()
            moving.update(bg_color, screen, main, enemies, ammos)
            moving.update_ammos(screen, enemies, ammos)
            moving.update_enemy(main, game_info, screen, ammos, enemies)


start()
