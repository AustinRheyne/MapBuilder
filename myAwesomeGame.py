import pygame
import mapBuilderLoader


pygame.init()
screen = pygame.display.set_mode((1280, 1280))

myMapLoader = mapBuilderLoader.MapLoader("Map - Sandy", screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    myMapLoader.display_map()

    pygame.display.flip()