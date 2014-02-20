import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((400,300))

    screen.fill((0, 0, 0))

    font = pygame.font.SysFont("monospace", 30)

    text = font.render("Hello World !", 1, (0, 255, 0))

    screen.blit(text, (40, 40))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

if __name__ == '__main__':
    main()
