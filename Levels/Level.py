import pygame as pg
import Config as Global
import csv
import os

class Tile(pg.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super(Tile, self).__init__()
        self.image = image.convert_alpha()
        self.image = pg.transform.scale(self.image, (Global.TILE_SIZE,Global.TILE_SIZE))
        self.x = x
        self.y = y
        self.mask = pg.mask.from_surface(self.image)
        
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
class TileMap():
    
    def __init__(self, filename):
        self.row = 0
        self.column = 0
        self.start_x = 0
        self.start_y = 0
        self.tile_map, map_dimensions = self.tile_load(filename)
        print(map_dimensions)
        self.map_surface = pg.Surface((self.map_width, self.map_height))
        self.map_surface.set_colorkey((0,0,0))
        
    def draw_map(self, surface):
        surface.blit(self.map_surface, (0,0))
        
    def load_map(self):
        for tile in self.tile_map:
            tile.draw(self.map_surface)

    def csv_load(self, filename):
        map = []
        
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter = ',')
            
            for row in data:
                map.append(list(row))
                
        return map
    
    def tile_load(self, filename):
        tiles = pg.sprite.Group()
        map = self.csv_load(filename)
        x, y = 0, 0
        
        for self.column, row in enumerate(map):
            x = 0
            #30-pipe-curve-top-left
            #1-pipeline-horizontal
            #4-pipe-curve-top-right
            #24-pipe-corner-bottom
            #26-pipe-corner-up
            #28-pipe-curve-bottom-left
            #29-pipe-curve-bottom-right
            for self.row, tile in enumerate(row):
                
                if tile == '0':
                    #nothing
                    pass
                
                elif tile == '30':
                    tiles.add(Tile(Global.PIPELINE_CURVE_TILE_TL, x * Global.TILE_SIZE, y * Global.TILE_SIZE))
                    
                elif tile == '1':
                    tiles.add(Tile(Global.PIPELINE_HORIZONTAL, x * Global.TILE_SIZE, y * Global.TILE_SIZE))
                    
                elif tile == '4':
                    tiles.add(Tile(Global.PIPELINE_CURVE_TILE_TR, x * Global.TILE_SIZE, y * Global.TILE_SIZE))
                    
                elif tile == '24':
                    tiles.add(Tile(Global.PIPELINE_CORNER_TILE_D, x * Global.TILE_SIZE, y * Global.TILE_SIZE))
                    
                elif tile == '26':
                    tiles.add(Tile(Global.PIPELINE_CORNER_TILE_U, x * Global.TILE_SIZE, y * Global.TILE_SIZE))
                    
                elif tile == '28':
                    tiles.add(Tile(Global.PIPELINE_CURVE_TILE_BL, x * Global.TILE_SIZE, y * Global.TILE_SIZE))
                    
                elif tile == '29':
                    tiles.add(Tile(Global.PIPELINE_CURVE_TILE_BR, x * Global.TILE_SIZE, y * Global.TILE_SIZE))
                
                x += 1
            y += 1    
        
        self.map_width, self.map_height = x * Global.TILE_SIZE, y * Global.TILE_SIZE
        return tiles, tuple([self.map_width, self.map_height])
    
    def get_collisions(self,tiles,obj):
        i = 0
        collisions = []
        
        for tile in tiles:
            if obj.player_inverted:
                collide_mask = tile.mask.overlap_mask(obj.mask, ((obj.x - 64) - tile.x, (obj.y - 64) - tile.y))
            else:
                collide_mask = tile.mask.overlap_mask(obj.mask, (obj.x - tile.x, obj.y - tile.y))
            
            if collide_mask.count() > 0:
                collisions.append(tile) 
                i+=1

        return i,collisions
     
    def check_collisions(self,tiles,obj):
        if type(obj) == list:
            for an_object in obj:
                i, collisions = self.get_collisions(tiles.tile_map, an_object)
            
                for tile in collisions:
                    
                    if not an_object.onGround:
                        print(an_object.isPlayer1)
                        if (tile.y * Global.TILE_SIZE > Global.SCREEN_HEIGHT):
                            an_object.player_inverted = False
                        
                        elif (tile.y * Global.TILE_SIZE < 0):
                            an_object.player_inverted = True
                        
                        an_object.onGround = True                
                
        else:    
            i, collisions = self.get_collisions(tiles.tile_map, obj)
        
            for tile in collisions:
                
                if not obj.onGround:
                    print(obj.isPlayer1)
                    if (tile.y * Global.TILE_SIZE > Global.SCREEN_HEIGHT):
                        obj.player_inverted = False
                        
                    elif (tile.y * Global.TILE_SIZE < 0):
                        obj.player_inverted = True
                        
                    obj.onGround = True 
            
                   