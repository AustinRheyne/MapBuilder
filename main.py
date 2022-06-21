
import pygame
import math
import os
import shutil
import tkinter as tk
from random import randint, random
from turtle import pu
from tile import Tile
from prefab import Prefab
from tkinter import filedialog
from moveManager import MoveManager
from fps import FPS


textures = "textures/"



# Begin TKinter stuff

tile_size = []
width = 0
height = 0
map_name = "My Map"

tex_dir = os.path.dirname(os.path.abspath(__file__)) + "/textures/"

window = tk.Tk()

tile_x_label = tk.Label(text = "Tile Width: ")
tile_x_entry = tk.Entry()
tile_x_label.pack()
tile_x_entry.pack()

tile_y_label = tk.Label(text = "Tile Height: ")
tile_y_entry = tk.Entry()
tile_y_label.pack()
tile_y_entry.pack()

map_x_label = tk.Label(text = "Map Width: ")
map_x_entry = tk.Entry()
map_x_label.pack()
map_x_entry.pack()

map_y_label = tk.Label(text = "Map Height: ")
map_y_entry = tk.Entry()
map_y_label.pack()
map_y_entry.pack()

map_name_label = tk.Label(text = "Map Name: ")
map_name_entry = tk.Entry()
map_name_label.pack()
map_name_entry.pack()


def begin():
    global tile_size
    global width
    global height
    global files
    global map_name
    tile_size = [int(tile_x_entry.get()), int(tile_y_entry.get())]
    width = int(map_x_entry.get())
    height = int(map_y_entry.get())
    map_name = map_name_entry.get()

    os.mkdir(tex_dir)

    for fname in files:
        shutil.copy2(fname, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'textures'))

    window.destroy()

files = ()

def uploadAction():
    global files
    files = filedialog.askopenfilenames()
    

flb = tk.Button(window, text="Select Textures", command = uploadAction)
flb.pack()

b = tk.Button(window, text="Create Map!", command=begin)
b.pack()

window.mainloop()


# --- Wait for all items to be input from TKinter --- #


pygame.init()
screen = pygame.display.set_mode((700, 900))



# --- Instantiation Conditions --- #

# Instantiate the tiles

manager = MoveManager()

row = 0
column = 0
tiles = []
prefabs = []


while len(tiles) < width*height:
    if column == width:
        column = 0
        row += 1
    tiles.append(Tile(column*tile_size[0], row*tile_size[1], tile_size[0], tile_size[1], column, row, 'blank.png', manager, screen))
    column += 1
print(len(tiles))
# Instantiate the prefabs
image_locations = {}

gap = 50
x = 0
y = 700 + gap
for file in os.listdir(textures):
    x += gap
    if x + tile_size[0] > 700-gap:
        x = 0
        y += gap
    prefabs.append(Prefab(x, y, tile_size[0], tile_size[1], textures + file, screen))
    x += tile_size[0]
    image_locations[textures+file] = ""

# --- Logic For Selecting and Using Tiles --- #
currentTile = None
mouseDown = False


fps = FPS()
def quitGame():
    for tile in tiles:
        if tile.image_path != "":
            position_string = f"[{tile.column},{tile.row}],"
            image_locations[tile.image_path] += position_string
            
    map_string = f"{tile_size}\n"
    for key in image_locations.keys():
        map_string += "{" + key +"} - [" + image_locations[key][:-1] + "]\n"

    # Create a new folder
    map_dir = os.path.dirname(os.path.abspath(__file__)) + "/Map - " + map_name
    os.mkdir(map_dir)

    # Move the textures into the map folder
    shutil.move(tex_dir, map_dir)

    # Create the map file
    with open(map_dir + '/map.AGR', 'w') as fp:
        pass

    fd = os.open(map_dir + '/map.AGR', os.O_RDWR)
    enc_str = str.encode(map_string)

    num_Bytes = os.write(fd, enc_str)

    pygame.quit()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitGame()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quitGame()
            if event.key == pygame.K_w:
                manager.up = True
            if event.key == pygame.K_s:
                manager.down = True
            if event.key == pygame.K_a:
                manager.right = True
            if event.key == pygame.K_d:
                manager.left = True
            if event.key == pygame.K_UP:
                manager.zoom = True
            if event.key == pygame.K_DOWN:
                manager.unzoom = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                manager.up = False
            if event.key == pygame.K_s:
                manager.down = False
            if event.key == pygame.K_a:
                manager.right = False
            if event.key == pygame.K_d:
                manager.left = False
            if event.key == pygame.K_UP:
                manager.zoom = False
            if event.key == pygame.K_DOWN:
                manager.unzoom = False
              
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseDown = True
                
            if event.button == 3:
                currentTile = None
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseDown = False

    screen.fill((0,0,0))

    manager.scale_tiles(tiles)

    for tile in tiles:
        tile.translate(manager.move_tiles())
        tile.update()

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 700, 700, 200))

    for prefab in prefabs:
        prefab.update()
    
    fps.render(screen)


    # Draw which tile is currently selected within the screen
    if currentTile:
        currentTileImage = currentTile.texture
        currentTileImage = pygame.transform.scale(currentTileImage, (10, 10))
        offset = (15, 15)
        currentTileRect = currentTileImage.get_rect()
        currentTileRect.x = pygame.mouse.get_pos()[0] + offset[0]
        currentTileRect.y = pygame.mouse.get_pos()[1] + offset[1]
        screen.blit(currentTileImage, currentTileRect)


    if mouseDown:
        for prefab in prefabs:
            if prefab.checkForClick(pygame.mouse.get_pos()):
                currentTile = prefab
        for tile in tiles:
            if currentTile != None:
                if tile.checkForClick(pygame.mouse.get_pos()):
                    tile.updateTexture(currentTile.image)




    pygame.display.flip()
    
    fps.clock.tick(120)