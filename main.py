import pygame, moving
from main_spaceship import Main
from pygame.sprite import Group
from game_info import Game_info
from scores import Scores



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
            main.update_gun()
            moving.update(bg_color, screen, stats, sc, main, enemies, ammos)
            moving.update_ammos(screen, stats, sc, enemies, ammos)
            moving.update_enemies(stats, screen, sc, main, enemies, ammos)

run()


