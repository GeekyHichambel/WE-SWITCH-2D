import pygame as pg
import Config as Global

class Player():
    
    def __init__(self, x, y, inverted = False):
        self.x = x
        self.y = y
        self.sprite_sheet = pg.image.load(Global.SPRITE_PATH + 'player_idle.png').convert_alpha()
        self.load_Scale()
        self.rect = self.image.get_rect(bottomleft = (self.x,self.y))
        self.animationFrame = 0
        self.onGround = False
        self.player_inverted = inverted
        
        if self.player_inverted:
            self.image = pg.transform.flip(self.image, False, True)

    def load_Scale(self):
        self.image = self.sprite_sheet.subsurface(pg.Rect(2 * Global.PLAYER_PIXEL_SIZE, 2 * Global.PLAYER_PIXEL_SIZE, Global.PLAYER_SIZE, Global.PLAYER_SIZE))
        self.image = pg.transform.scale(self.image, (64,64))
        
    def draw(self, surface):     
        surface.blit(self.image, self.rect)
        
    def update(self):
                        
        if self.onGround:
            self.animate(Global.PLAYER_IDLE_SPEED)
            
        else:
            if self.player_inverted:
                self.rect.y -= Global.GRAVITY
                
            else:
                self.rect.y += Global.GRAVITY
                
        if self.rect.y > Global.SCREEN_HEIGHT - 64 :
            self.rect.y = Global.SCREEN_HEIGHT - 64 
            self.player_inverted = False
            self.onGround = True
            
        elif self.rect.y < 0:
            self.rect.y = 0
            self.player_inverted = True
            self.onGround = True
        
    def move(self, action):
        
        if action == 'FLIP':
            self.onGround = False
            self.load_Scale()
            
            if not self.player_inverted:
                self.image = pg.transform.flip(self.image, False, True)
                
            self.player_inverted = not self.player_inverted
                
    def animate(self, speed):
        self.animationFrame += speed
            
        if self.animationFrame >= 4:
            self.animationFrame = 0
            
        self.image = self.sprite_sheet.subsurface(pg.Rect((2 * Global.PLAYER_PIXEL_SIZE) + (int(self.animationFrame) * 1000), 2 * Global.PLAYER_PIXEL_SIZE, Global.PLAYER_SIZE, Global.PLAYER_SIZE))
        self.image = pg.transform.scale(self.image, (64,64))
        
        if self.player_inverted:
            self.image = pg.transform.flip(self.image, False, True)
         