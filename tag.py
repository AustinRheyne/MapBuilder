import pygame
import random
from prefab import Prefab

pygame.font.init()
class TagButton:
    def __init__(self, screen, image, x, y, w, h):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.screen.blit(self.image, self.rect)

    def checkForClick(self, m):
        mX, mY = m
        if self.rect.left < mX < self.rect.right and self.rect.top < mY < self.rect.bottom:
            return True
        return False 


class Tag(Prefab):
    def __init__(self, x, y, w, h, screen, name):
        super().__init__(x, y, w, h, "blank.png", screen)
        self.font = pygame.font.SysFont('Comic Sans MS', 25)
        self.name = name
        self.color = (random.randint(0, 225), random.randint(0, 225), random.randint(0, 225))

    def draw(self):
        self.texture.fill(self.color)
        self.update()
        self.txt_box = self.font.render(self.name, False, (0,0,0))
        self.txt_box_rect = self.txt_box.get_rect()
        self.txt_box_rect.center = self.rect.center
        self.screen.blit(self.txt_box, self.txt_box_rect)
