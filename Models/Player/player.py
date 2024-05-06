import pygame as pg
from Config import *

class Player():
    
    def __init__(self, x, y, inverted = False):
        self.x = x
        self.y = y
        self.sprite_sheet = pg.image.load(SPRITE_PATH + 'player_idle.png').convert_alpha()
        self.image = self.sprite_sheet.subsurface(pg.Rect(2 * PLAYER_PIXEL_SIZE, 2 * PLAYER_PIXEL_SIZE, PLAYER_SIZE, PLAYER_SIZE))
        self.image = pg.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect(bottomleft = (self.x,self.y))
        self.animationFrame = 0
        self.onGround = False
        self.player_inverted = inverted
        
        if self.player_inverted:
            self.image = pg.transform.flip(self.image, False, True)
        
    def draw(self, surface):     
        surface.blit(self.image, self.rect)
        
    def update(self):
                        
        if self.onGround:
            self.animate(PLAYER_IDLE_SPEED)
            
        else:
            if self.player_inverted:
                self.rect.y -= GRAVITY
                
            else:
                self.rect.y += GRAVITY
                
        if self.rect.y > SCREEN_HEIGHT - 64:
            self.rect.y = SCREEN_HEIGHT - 64
            self.player_inverted = False
            self.onGround = True
            
        elif self.rect.y < 0:
            self.rect.y = 0
            self.player_inverted = True
            self.onGround = True
        
    def move(self, action):
        
        if action == 'FLIP':
            self.onGround = False
            self.image = self.sprite_sheet.subsurface(pg.Rect(2 * PLAYER_PIXEL_SIZE, 2 * PLAYER_PIXEL_SIZE, PLAYER_SIZE, PLAYER_SIZE))
            self.image = pg.transform.scale(self.image, (64,64))
            
            if not self.player_inverted:
                self.image = pg.transform.flip(self.image, False, True)
                
            self.player_inverted = not self.player_inverted
                
    def animate(self, speed):
        self.animationFrame += speed
            
        if self.animationFrame >= 4:
            self.animationFrame = 0
            
        self.image = self.sprite_sheet.subsurface(pg.Rect((2 * PLAYER_PIXEL_SIZE) + (int(self.animationFrame) * 1000), 2 * PLAYER_PIXEL_SIZE, PLAYER_SIZE, PLAYER_SIZE))
        self.image = pg.transform.scale(self.image, (64,64))
        
        if self.player_inverted:
            self.image = pg.transform.flip(self.image, False, True)
         