# STEP 1: INSTALL AND IMPORT PYGAME
import pygame
import sys

# STEP 2: SETUP THE GAME LOOP
""" How to initialise Pygame. You have to initialise the clock outside the
while loop. """
pygame.init()
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

""" While loop ensures the game is running forever until we close it. """
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    colour = (41, 46, 57)
    screen.fill(colour)
    pygame.display.update()
    clock.tick(60)

# STEP 3: CREATE THE GRID


# STEP 4: CREATE THE BLOCKS

# STEP 5: MOVE THE BLOCKS

# STEP 6: ROTATE THE BLOCKS

# STEP 7: CHECKING FOR COLLISIONS

# STEP 8: CHECK FOR COMPLETED ROWS

# STEP 9: GAME OVER

# STEP 10: Create UUI

# STEP 11: ADD SCORE

# STEP 12: ADD NEXT BLOCK

# STEP 13: ADD SOUNDS
