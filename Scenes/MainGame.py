import pygame as pg
from Models.Player import player
import Config as Global

class MainGame():
    
    def __init__(self):
        self.background = pg.image.load(Global.IMAGE_PATH + 'background.png').convert()
        self.background = pg.transform.scale(self.background, (Global.SCREEN_WIDTH, Global.SCREEN_HEIGHT))
        self.player1 = player.Player(100, 450, inverted= True)
        self.player2 = player.Player(100, 514)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.player1.draw(screen)
        self.player2.draw(screen)
        
    def update(self):        
        self.player1.update()
        self.player2.update()

    def run(self, screen):
        
        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                Global.gAME_STATE = False
                
            elif event.type == pg.KEYDOWN:
                
                if event.key == Global.QUIT_KEY:
                    Global.gAME_STATE = False
                    
                if event.key == Global.FULLSCREEN_KEY:
                    Global.iS_FULLSCREEN = not Global.iS_FULLSCREEN 
                    screen = pg.display.set_mode((Global.SCREEN_WIDTH, Global.SCREEN_HEIGHT),pg.FULLSCREEN if Global.iS_FULLSCREEN else 0)    
                    
                if event.key == Global.PLAYER1_KEY:
                    self.player1.move(action= 'FLIP')
                    
                if event.key == Global.PLAYER2_KEY:
                    self.player2.move(action= 'FLIP')
                    
        self.update()
        self.draw(screen= screen)       