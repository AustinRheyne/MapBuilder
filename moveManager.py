class MoveManager:
    def __init__(self):
        self.speed = 15
        self.zoom_speed = 1
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.zoom = False
        self.unzoom = False
        self.current_zoom = 1


    def move_tiles(self):
        x,y = 0, 0
        if self.left:
            x -= self.speed
        if self.right:
            x += self.speed
        if self.down:
            y -= self.speed
        if self.up:
            y += self.speed
        
        return (x, y)

    def scale_tiles(self, tiles):
        if self.zoom == True:
            self.current_zoom += self.zoom_speed
        if self.unzoom == True:
            self.current_zoom -= self.zoom_speed
        
        if self.zoom or self.unzoom:
            x_offset = tiles[0].rect.x
            y_offset = tiles[0].rect.y
            for tile in tiles:
                tile.scale(self.current_zoom)
                tile.new_pos((tile.column*(tile.w+self.current_zoom)+x_offset, tile.row*(tile.h+self.current_zoom)+y_offset))
