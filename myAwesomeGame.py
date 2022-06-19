import pygame
import mapBuilderLoader


pygame.init()
screen = pygame.display.set_mode((600, 900))

myMapLoader = mapBuilderLoader.MapLoader("Map - Block Breaker", screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    
    myMapLoader.display_map()

    pygame.display.flip()