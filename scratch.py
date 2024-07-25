import pygame
import sys

pygame.init()
""" How to initialise Pygame. You have to initialise the clock outside the
while loop. """
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

""" While loop ensures the game is running forever until we close it. """
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
