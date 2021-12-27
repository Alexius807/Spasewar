import pygame
import sys
from Main_spaceship import Main_spaseship


def start():
    pygame.init()
    screen = pygame.display.set_mode((1400, 1000))
    pygame.display.set_caption('Spase war')
    bg_color = (0, 0, 0)
    main = Main_spaseship(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        main.run_main()
        pygame.display.flip()


start()