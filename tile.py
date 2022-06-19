
import pygame

class Tile:
    def __init__(self, x, y, w, h, c, r, texture, screen):
        self.w = w
        self.h = h
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.screen = screen
        self.texture.fill((0,0,0))
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image_path = ""

        self.column = c
        self.row = r
    def update(self):
        self.screen.blit(self.texture, self.rect)

    def updateTexture(self, image):
        x, y = self.rect.x, self.rect.y
        self.texture = pygame.image.load(image)
        self.texture = pygame.transform.scale(self.texture, (self.w, self.h))
        self.rect = self.texture.get_rect()
        self.rect.x, self.rect.y = x, y
        self.image_path = image
    def checkForClick(self, m):
        mX, mY = m
        if self.rect.left < mX < self.rect.right and self.rect.top < mY < self.rect.bottom:
            return True
        return False 
