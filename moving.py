import pygame, sys
from ammo import Ammo
from enemy import Enemy
import time


# Нажатия клавишь
def events(screen, main, ammos):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                main.mright = True
            elif event.key == pygame.K_a:
                main.mleft = True
            elif event.key == pygame.K_SPACE:
                new_ammo = Ammo(screen, main)
                ammos.add(new_ammo)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                main.mright = False
            elif event.key == pygame.K_a:
                main.mleft = False


def update(bg_color, screen, stats, sc, main, enemies, ammos):
    screen.fill(bg_color)
    sc.show_score()
    for ammo in ammos.sprites():
        ammo.draw_ammo()
    main.draw_main()
    enemies.draw(screen)
    pygame.display.flip()


# начало атаки новой армии
def start_attack(screen, enemies):
    enemy = Enemy(screen)
    en_width = enemy.rect.width
    number_en_x = int((700 - 2 * en_width) / en_width)
    en_height = enemy.rect.height
    number_en_y = int((800 - 100 - 2 * en_height) / en_height)

    for row_number in range(number_en_y - 3):
        for en_number in range(number_en_x):
            en = Enemy(screen)
            en.x = en_width + (en_width * en_number)
            en.y = en_height + (en_height * row_number)
            en.rect.x = en.x
            en.rect.y = en.rect.height + (en.rect.height * row_number)
            enemies.add(en)


# обновление снарядов
def update_ammos(screen, stats, sc, enemies, ammos):
    ammos.update()
    for ammo in ammos.copy():
        if ammo.rect.bottom <= 0:
            ammos.remove(ammo)
    collisions = pygame.sprite.groupcollide(ammos, enemies, True, True)
    if collisions:
        for enemies in collisions.values():
            stats.score += 10 * len(enemies)
        sc.image_score()
        check_record(stats, sc)
        sc.show_lives()
    if len(enemies) == 0:
        ammos.empty()
        start_attack(screen, enemies)


# позиция врага
def update_enemies(stats, screen, sc, main, enemies, ammos):
    enemies.update()
    if pygame.sprite.spritecollideany(main, enemies):
        main_loose(stats, screen, sc, main, enemies, ammos)
    check_enemies(stats, screen, sc, main, enemies, ammos)


# поражение если враги дошли до нижнего края экрана
def check_enemies(stats, screen, sc, main, enemies, ammos):
    screen_rect = screen.get_rect()
    for ino in enemies.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            main_loose(stats, screen, sc, main, enemies, ammos)
            break


# проверка рекорда
def check_record(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.show_record()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))


# если враг касается игрока
def main_loose(stats, screen, sc, main, enemies, ammos):
    if stats.main_lives > 0:
        stats.main_lives -= 1
        sc.show_lives()
        enemies.empty()
        ammos.empty()
        start_attack(screen, enemies)
        main.ressurect_main()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()
