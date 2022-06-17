from random import randint, random
from turtle import pu
from tile import Tile
from prefab import Prefab
import pygame
import math
import os

pygame.init()
screen = pygame.display.set_mode((700, 900))

tile_size = [16, 16]
width = 10
height = 10

textures = "textures/"

# --- Instantiation Conditions --- #

# Instantiate the tiles
scaled_w = 700/width
scaled_h = 700/height

row = 0
column = 0
tiles = []
prefabs = []

while len(tiles) < width*height:
    if column == width:
        column = 0
        row += 1
    tiles.append(Tile(column * scaled_w, row*scaled_h, scaled_w, scaled_h, 'blank.png', screen))
    column += 1

print(tiles)

# Instantiate the prefabs
gap = 50
x = 0
y = 700 + gap
for file in os.listdir(textures):
    x += gap
    if x + scaled_w > 700-gap:
        x = 0
        y += gap
    prefabs.append(Prefab(x, y, scaled_w, scaled_h, textures + file, screen))
    x += scaled_w

# --- Logic For Selecting and Using Tiles --- #
currentTile = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for prefab in prefabs:
                    if prefab.checkForClick(pygame.mouse.get_pos()):
                        currentTile = prefab
            if event.button == 3:
                currentTile = None
    
    screen.fill((255,255,255))

    for tile in tiles:
        tile.update()

    for prefab in prefabs:
        prefab.update()
        



    # Draw which tile is currently selected within the screen
    if currentTile:
        currentTileImage = currentTile.texture
        currentTileImage = pygame.transform.scale(currentTileImage, (10, 10))
        offset = (15, 15)
        currentTileRect = currentTileImage.get_rect()
        currentTileRect.x = pygame.mouse.get_pos()[0] + offset[0]
        currentTileRect.y = pygame.mouse.get_pos()[1] + offset[1]
        screen.blit(currentTileImage, currentTileRect)


    pygame.draw.line(screen, (0,0,0), (0, 700), (700, 700), 5)

    pygame.display.flip()