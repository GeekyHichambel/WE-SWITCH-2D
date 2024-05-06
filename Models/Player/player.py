import pygame as pg
from Config import *

class Player():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sprite_sheet = pg.image.load(ASSETS_PATH + 'sprites/player_idle.png').convert_alpha()
        self.image = self.sprite_sheet.subsurface(pg.Rect(2 * PLAYER_PIXEL_SIZE, 2 * PLAYER_PIXEL_SIZE, PLAYER_SIZE, PLAYER_SIZE))
        self.image = pg.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(bottomleft = (self.x,self.y))
        self.animationFrame = 0
        self.state = 'IDLE'
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
    def update(self):
        if self.state == 'IDLE':
            self.animate(PLAYER_IDLE_SPEED)
        
    def move(self):
        pass
    
    def animate(self, speed):
        self.animationFrame += speed
            
        if self.animationFrame >= 4:
            self.animationFrame = 0
            
        self.image = self.sprite_sheet.subsurface(pg.Rect((2 * PLAYER_PIXEL_SIZE) + (int(self.animationFrame) * 1000), 2 * PLAYER_PIXEL_SIZE, PLAYER_SIZE, PLAYER_SIZE))
        self.image = pg.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(bottomleft = (self.x,self.y))
         