import sys, pygame
import time

from ammo import Ammo
from enemy import Enemy


def check_events(screen, main, ammos):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                main.right_move = True
            elif event.key == pygame.K_a:
                main.left_move = True
            elif event.key == pygame.K_SPACE:
                new_ammo = Ammo(screen, main)
                ammos.add(new_ammo)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                main.right_move = False
            elif event.key == pygame.K_a:
                main.left_move = False
        elif event.type == pygame.QUIT:
            sys.exit()


def update(bg_color, screen, main, enemies, ammos):
    screen.fill(bg_color)
    for ammo in ammos.sprites():
        ammo.draw()
    main.run_main()
    enemies.draw_enemy(screen)
    pygame.display.flip()


def update_ammos(screen, ammos, enemies):
    ammos.update()
    for ammo in ammos.copy():
        if ammo.rect.bottom <= 0:
            ammos.remove(ammo)
    colide = pygame.sprite.groupcollide(ammos, enemies, True, True)
    if len(enemies) == 0:
        ammos.empty()
        start_attack(screen, enemies)


def start_attack(screen, enemies):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    enemy_row = int((700 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_of_rows = int((800 - 200 - 2 * enemy_height) / enemy_height)

    for row in range(number_of_rows - 1):
        for i in range(enemy_row):
            enemy = Enemy
            enemy.x = enemy_width + enemy_width * i
            enemy.y = enemy_height + enemy_height * row
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + enemy.rect.height * row
            enemies.add(enemy)


def update_enemy(main, game_info, screen, ammos, enemies):
    enemies.update()
    if pygame.sprite.spritecollideany(main, enemies):
        main_loose(game_info, screen, main, enemies, ammos)
    check_borders(game_info, screen, enemies, ammos, main)


def main_loose(game_info, screen, main, enemies, ammos):
    if game_info.main_lives > 0:
        game_info.main_lives -= 1
        enemies.empty()
        ammos.empty()
        start_attack(screen, enemies)
        main.resurrect_main()
        time.sleep(3)
    else:
        game_info.start = False
        sys.exit()

def check_borders(game_info, screen, enemies, ammos, main):
    screen_rect = screen.get_rect()
    for i in enemies.sprites():
        if i.rect.bottom >= screen_rect.bottom:
            main_loose(game_info, screen, main, enemies, ammos)
            break
