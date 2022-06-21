
import pygame

class Tile:
    def __init__(self, x, y, w, h, c, r, texture, manager, screen):
        self.w = w
        self.h = h
        self.image_path = texture
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.screen = screen
        self.texture.fill((0,0,0))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.column = c
        self.row = r

        self.manager = manager
    def update(self):
        self.screen.blit(self.texture, self.rect)

    def updateTexture(self, image):
        x, y = self.rect.x, self.rect.y
        self.texture = pygame.image.load(image)
        self.texture = pygame.transform.scale(self.texture, (self.w+self.manager.current_zoom, self.h+self.manager.current_zoom))
        self.rect = self.texture.get_rect()
        self.rect.x, self.rect.y = x, y
        self.image_path = image

    def translate(self, dir):
        # Direction -> (x, y)
        self.rect.x += dir[0]
        self.rect.y += dir[1]
    
    def scale(self, amount):
        x = self.rect.x
        y = self.rect.y
        self.texture = pygame.image.load(self.image_path)
        self.texture = pygame.transform.scale(self.texture, (self.w+amount, self.h+amount))
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
