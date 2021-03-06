import pygame

class Prefab:
    def __init__(self, x, y, w, h, texture, screen):
        self.image = texture
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.screen = screen
        self.rect = self.texture.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.screen.blit(self.texture, self.rect)

    def checkForClick(self, m):
        mX, mY = m
        if self.rect.left < mX < self.rect.right and self.rect.top < mY < self.rect.bottom:
            return True
        return False 
