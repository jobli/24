import pygame, sys

from pygame.locals import *

RED = (255, 0, 0)

BLACK = (0, 0, 0)

def main():
    pygame.init()

    screen = pygame.display.set_mode((400,300))

    x = 20
    y = 20

    pygame.draw.rect(screen, BLACK, (0, 0, 400, 300))
    pygame.draw.circle(screen, RED, (x, y), 10)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x -= 10
                elif event.key == K_RIGHT:
                    x += 10
                elif event.key == K_UP:
                    y -= 10
                elif event.key == K_DOWN:
                    y += 10

        pygame.draw.rect(screen, BLACK, (0, 0, 400, 300))
        pygame.draw.circle(screen, RED, (x, y), 10)
        pygame.display.update()

if __name__ == '__main__':
    main()
