# forgive me uncle bob

import pygame, sys
from pygame.locals import *
import time

DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
GOAL = 4

# constants representing colours
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

types = {"Dreck": 0, "Gras": 1, "Wasser": 2, "Kohle": 3, "Ziel": 4}
types_revers = {v: k for k, v in types.items()}

direction_vectors = {"Links": [-1, 0], "Rechts": [1, 0], "Hoch": [0, -1], "Runter": [0, 1], "noop": [0, 0]}
# a dictionary linking resources to textures
textures = {
    DIRT: pygame.image.load('library/dirt.png'),
    GRASS: pygame.image.load('library/grass.png'),
    WATER: pygame.image.load('library/water.png'),
    COAL: pygame.image.load('library/coal.png'),
    GOAL: pygame.image.load('library/goal.png')
}

# useful game dimensions
TILESIZE = 40
MAPWIDTH = 10
MAPHEIGHT = 10

tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

moves = ["noop"]

resources = [DIRT, GRASS, COAL]


def bewegung(move):
    moves.append(move)


def set_size(width, height):
    global tilemap
    global MAPHEIGHT
    global MAPWIDTH
    tilemap = [[DIRT for w in range(width)] for h in range(height)]
    MAPWIDTH = width
    MAPHEIGHT = height


def block(x_position, y_position, block_type):
    try:
        tilemap[y_position][x_position] = types[block_type]
    except IndexError:
        print("So groß ist dein labyrinth nicht")


def block_typ(x_position, y_position):
    if x_position < 0 or y_position < 0 or x_position > MAPWIDTH or y_position > MAPHEIGHT:
        return "Nichts"
    return types_revers[tilemap[y_position][x_position]]


def start():
    # a list of resources
    # use list comprehension to create our tilemap
    coal_counter = 0
    found_coal = []
    # set up the display
    pygame.init()
    INVFONT = pygame.font.Font('library/Minecraftia.ttf', 18)
    DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))

    # the player image
    PLAYER = pygame.image.load('library/player_female.png').convert_alpha()
    # the position of the player [x,y]

    i = 0
    while True:
        if i == 0:
            player_pos = [0, 0]
            coal_counter = 0
            found_coal = []

        move = moves[i] if len(moves) > 0 else "noop"

        player_pos[0] += direction_vectors[move][0]
        player_pos[1] += direction_vectors[move][1]

        i = i + 1 if i < len(moves) - 1 else 0  # i want to repeat the animation
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
        DISPLAYSURF.blit(PLAYER, (player_pos[0] * TILESIZE, player_pos[1] * TILESIZE))

        textObj = INVFONT.render("Kohle: " + str(coal_counter), True, WHITE, BLACK)
        DISPLAYSURF.blit(textObj, (10, MAPHEIGHT * TILESIZE - 30))

        pygame.display.update()
        time.sleep(1)

        current_code = tilemap[player_pos[1]][player_pos[0]]

        if current_code == GOAL:
            textObj = INVFONT.render("Geschafft!", True, WHITE, BLACK)
            DISPLAYSURF.blit(textObj, (10, MAPHEIGHT * TILESIZE - 30))

        elif current_code == COAL and not tuple(player_pos) in found_coal:
            coal_counter += 1
            found_coal.append(tuple(player_pos))
            textObj = INVFONT.render("Kohle: " + str(coal_counter), True, WHITE, BLACK)
            DISPLAYSURF.blit(textObj, (10, MAPHEIGHT * TILESIZE - 30))
        elif current_code == WATER:
            textObj = INVFONT.render("Du kannst nicht über Wasser gehen!", True, WHITE, BLACK)
            DISPLAYSURF.blit(textObj, (10, MAPHEIGHT * TILESIZE - 30))
            pygame.display.update()
            i = 0
            continue
        pygame.display.update()


if __name__ == '__main__':
    start()
