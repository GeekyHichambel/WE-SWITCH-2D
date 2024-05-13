import pygame as pg
import Config as Global

class Player():
    
    def __init__(self, x, y, inverted = False):
        self.x = x
        self.y = y
        self.sprite_sheet = pg.image.load(Global.SPRITE_PATH + 'player_run.png').convert_alpha()
        self.sprite_sheet_2 = pg.image.load(Global.SPRITE_PATH + 'player2_run.png').convert_alpha()
        self.isPlayer1 = inverted
        self.load_Scale()
        self.rect = self.image.get_rect(bottomleft = (self.x,self.y))
        self.animationFrame = 0
        self.onGround = False
        self.player_inverted = inverted
        
        if self.player_inverted:
            self.image = pg.transform.flip(self.image, False, True)
            self.mask = pg.mask.from_surface(self.image)

    def load_Scale(self):
        
        if self.isPlayer1:
            self.image = self.sprite_sheet_2.subsurface(pg.Rect(Global.PLAYER_PIXEL_SIZE, Global.PLAYER_PIXEL_SIZE, Global.PLAYER_SIZE, Global.PLAYER_SIZE))
            
        else:
            self.image = self.sprite_sheet.subsurface(pg.Rect(Global.PLAYER_PIXEL_SIZE, Global.PLAYER_PIXEL_SIZE, Global.PLAYER_SIZE, Global.PLAYER_SIZE))
            
        self.image = pg.transform.scale(self.image, (64,64))  
        self.mask = pg.mask.from_surface(self.image) 
        
    def draw(self, surface):     
        surface.blit(self.image, self.rect)
        
    def update(self):
                        
        if self.onGround:
            self.animate(Global.PLAYER_RUN_SPEED)
            
        else:
            if self.player_inverted:
                self.rect.y -= Global.GRAVITY
                
            else:
                self.rect.y += Global.GRAVITY
                
        if self.rect.y > Global.SCREEN_HEIGHT - 64 :
            print('Went Offscreen')
            # self.rect.y = Global.SCREEN_HEIGHT - 64 
            # self.player_inverted = False
            # self.onGround = True
            
        elif self.rect.y < 0:
            print('Went Offscreen')
            # self.rect.y = 0
            # self.player_inverted = True
            # self.onGround = True
        
    def move(self, action):
        
        if action == 'FLIP':
            self.onGroundTime = None
            self.onGround = False
            self.load_Scale()
            
            if not self.player_inverted:
                self.image = pg.transform.flip(self.image, False, True)
                
            self.player_inverted = not self.player_inverted
                
    def animate(self, speed):
        self.animationFrame += speed
            
        if self.animationFrame >= 4:
            self.animationFrame = 0
        
        if self.isPlayer1:
            self.image = self.sprite_sheet_2.subsurface(pg.Rect(Global.PLAYER_PIXEL_SIZE + (int(self.animationFrame) * 1000), Global.PLAYER_PIXEL_SIZE, Global.PLAYER_SIZE, Global.PLAYER_SIZE))
            
        else:
            self.image = self.sprite_sheet.subsurface(pg.Rect(Global.PLAYER_PIXEL_SIZE + (int(self.animationFrame) * 1000), Global.PLAYER_PIXEL_SIZE, Global.PLAYER_SIZE, Global.PLAYER_SIZE))
           
        self.image = pg.transform.scale(self.image, (64,64))
        self.mask = pg.mask.from_surface(self.image)
        
        if self.player_inverted:
            self.image = pg.transform.flip(self.image, False, True)
            self.mask = pg.mask.from_surface(self.image)
         