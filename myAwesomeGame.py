import pygame
import mapBuilderLoader


pygame.init()
screen = pygame.display.set_mode((500, 500))

myMapLoader = mapBuilderLoader.MapLoader("Map - ExampleMap", screen, 6)
monsterSpawnLocations = myMapLoader.find_tiles_by_tag("MonsterSpawn")
entrance = myMapLoader.find_tiles_by_tag("Entrance")[0]
exit = myMapLoader.find_tiles_by_tag("Exit")[0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    myMapLoader.display_map()

    mousePos = pygame.mouse.get_pos()

    if entrance.collides_with(mousePos):
        myMapLoader.outline_tile(entrance, (0, 255, 0), 3)

    if exit.collides_with(mousePos):
        myMapLoader.outline_tile(exit, (255, 0, 0), 3)

    for tile in monsterSpawnLocations:
        if tile.collides_with(mousePos):
            myMapLoader.outline_tile(tile, (255, 255, 0), 3)

    
    

    pygame.display.flip()