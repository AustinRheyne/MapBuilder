import pygame
class FPS:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(round(self.clock.get_fps())), True, (255, 225, 0))

    def render(self, screen):
        self.text = self.font.render(str(round(self.clock.get_fps())), True, (255, 225, 0))
        screen.blit(self.text, (5, 5))