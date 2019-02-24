import pygame, sys
from pygame.locals import *
import time

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3

types = {"dirt": 0, "grass": 1, "water": 2, "coal": 3}

# a dictionary linking resources to textures
textures = {
    DIRT: pygame.image.load('library/dirt.png'),
    GRASS: pygame.image.load('library/grass.png'),
    WATER: pygame.image.load('library/water.png'),
    COAL: pygame.image.load('library/coal.png')
}

# useful game dimensions
TILESIZE = 20
MAPWIDTH = 30
MAPHEIGHT = 30

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]


def add_block(x_position, y_position, block_type):
    tilemap[x_position][y_position] = types[block_type]


def draw_labyrinth():
    # a list of resources
    # use list comprehension to create our tilemap

    # set up the display
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))

    # the player image
    PLAYER = pygame.image.load('library/player.png').convert_alpha()
    # the position of the player [x,y]
    playerPos = [0, 0]

    while True:

        # get all the user events
        for event in pygame.event.get():
            # if the user wants to quit
            if event.type == QUIT:
                # and the game and close the window
                pygame.quit()
                sys.exit()

        # loop through each row
        for row in range(MAPHEIGHT):
            # loop through each column in the row
            for column in range(MAPWIDTH):
                # draw the resource at that position in the tilemap, using the correct image
                DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
                # display the player at the correct position
                DISPLAYSURF.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))

        time.sleep(1)
        playerPos[0] += 1
        # update the display
        pygame.display.update()


if __name__ == '__main__':
    draw_labyrinth()
