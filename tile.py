
import pygame

class Tile:
    def __init__(self, x, y, w, h, c, r, texture, manager, screen):
        self.w = w
        self.h = h

        self.currentW = w
        self.currentH = h

        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.screen = screen
        self.texture.fill((0,0,0))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.tag = ""
        self.tagRefrence = None

        self.column = c
        self.row = r

        self.image_path = ""
        self.manager = manager

    def draw_grid(self):
        width = 1
        pygame.draw.line(self.screen, (255, 255, 255), (self.rect.x, self.rect.y), (self.rect.x + self.currentW, self.rect.y), width)
        pygame.draw.line(self.screen, (255, 255, 255), (self.rect.x+self.currentW, self.rect.y), (self.rect.x + self.currentW, self.rect.y + self.currentH), width)
        pygame.draw.line(self.screen, (255, 255, 255), (self.rect.x + self.currentW, self.rect.y + self.currentH), (self.rect.x, self.rect.y+self.currentH), width)
        pygame.draw.line(self.screen, (255, 255, 255), (self.rect.x, self.rect.y+self.currentH), (self.rect.x, self.rect.y), width)
    def update(self):
        if self.tag:
            # Scale the tag image
            scaled_texture = pygame.transform.scale(self.tagRefrence.texture, (self.w+self.manager.current_zoom, self.h+self.manager.current_zoom))
            # Change the transparency
            scaled_texture.set_alpha(128)
            # Apply
            self.texture.blit(scaled_texture, (0,0))
        self.screen.blit(self.texture, self.rect)
        if self.image_path == "":
            self.draw_grid()

    def updateTexture(self, image):
        x, y = self.rect.x, self.rect.y
        self.texture = pygame.image.load(image)
        self.texture = pygame.transform.scale(self.texture, (self.w+self.manager.current_zoom, self.h+self.manager.current_zoom))
        self.rect = self.texture.get_rect()
        self.rect.x, self.rect.y = x, y
        self.image_path = image
        self.tag = ""

    def translate(self, dir):
        # Direction -> (x, y)
        self.rect.x += dir[0]
        self.rect.y += dir[1]
    
    def scale(self, amount):

        path = self.image_path
        if self.image_path == "":
            path = "blank.png"

        x = self.rect.x
        y = self.rect.y
        self.currentW = self.w + amount
        self.currentH = self.h + amount
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.currentW, self.currentH))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def new_pos(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def checkForClick(self, m):
        mX, mY = m
        if self.rect.left < mX < self.rect.right and self.rect.top < mY < self.rect.bottom:
            return True
        return False 
