import pygame
import json

class MapLoader:
    def __init__(self, folder, screen, scale = 1):
        fd = open(folder+"/map.AGR", 'r')
        lines = fd.readlines()

        self.screen = screen

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
                    tag = ""
                    #Nessecary to continue using the tag system
                    try:
                        tag = pos[2]
                    except:
                        pass
                    self.tiles.append(Tile(round(dimensions[0]*self.map_scale), round(dimensions[1]*self.map_scale), pos[0], pos[1], folder + "/" + text, tag, screen))
            currentLine += 1
    def display_map(self):
        for tile in self.tiles:
            tile.update()
    
    def find_tiles_by_tag(self, tag):
        tiles = []
        for tile in self.tiles:
            if tile.tag == tag:
                tiles.append(tile)
        
        return tiles

    def outline_tile(self, tile, color, width = 1):
        pygame.draw.line(self.screen, color, tile.rect.topleft, tile.rect.topright, width)
        pygame.draw.line(self.screen, color, tile.rect.topright, tile.rect.bottomright, width)
        pygame.draw.line(self.screen, color, tile.rect.bottomright, tile.rect.bottomleft, width)
        pygame.draw.line(self.screen, color, tile.rect.bottomleft, tile.rect.topleft, width)

    

class Tile:
    def __init__(self, w, h, c, r, texture, tag, screen):
        self.tag = tag
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

    def collides_with(self, pos):
        if self.rect.x < pos[0] < self.rect.x + self.w:
            if self.rect.y < pos[1] < self.rect.y + self.h:
                return True

