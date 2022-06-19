import pygame
import json

class MapLoader:
    def __init__(self, folder, screen, scale = 1):
        fd = open(folder+"/map.AGR", 'r')
        lines = fd.readlines()

        self.map_scale = scale
        self.tiles = []
        currentLine = 0

        dimensions = json.loads(lines[0])

        for line in lines:
            if currentLine != 0:
                text = ""
                count = 0
                for char in line:
                    if char == "}":
                        count += 3
                        break
                    if char != "{":
                        text += char
                    count += 1
                print(text)
                positions = json.loads(line[count:])
                for pos in positions:
                    self.tiles.append(Tile(round(dimensions[0]*self.map_scale), round(dimensions[1]*self.map_scale), pos[0], pos[1], folder + "/" + text, screen))
            currentLine += 1
    def display_map(self):
        for tile in self.tiles:
            tile.update()


class Tile:
    def __init__(self, w, h, c, r, texture, screen):
        self.w = w
        self.h = h
        self.column = c
        self.row = r
        self.image_path = texture
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.screen = screen
        self.rect = self.texture.get_rect()
        self.rect.x = w * c
        self.rect.y = h * r


    def update(self):
        self.screen.blit(self.texture, self.rect)



