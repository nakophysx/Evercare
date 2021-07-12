import gscene
import pygame
import sys

bg = None
ch = None
screen_size = None


def init(size):
    global screen_size

    pygame.init()
    screen = pygame.display.set_mode(size)
    screen_size = size
    return screen


# MAIN GAME LOOP #


def run(screen):
    global bg
    global ch
    global screen_size

    my_scene = gscene.GScene("1.jpg")
    bg = pygame.transform.smoothscale(my_scene.get_bg(), screen_size)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # DRAW #
        screen.blit(bg, (0, 0))
        pygame.display.flip()
