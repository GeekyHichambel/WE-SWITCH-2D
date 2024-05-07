import pygame as pg
from Models.Player import player
from Config import *

class MainGame():
    
    def __init__(self):
        self.background = pg.image.load(IMAGE_PATH + 'background.png').convert()
        self.background = pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player1 = player.Player(100, 300, inverted= True)
        self.player2 = player.Player(100, 364)

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
                GAME_STATE = False
                
            elif event.type == pg.KEYDOWN:
                
                if event.key == pg.K_ESCAPE:
                    GAME_STATE = False
                    
                if event.key == PLAYER1_KEY:
                    self.player1.move(action= 'FLIP')
                    
                if event.key == PLAYER2_KEY:
                    self.player2.move(action= 'FLIP')
                    
        self.update()
        self.draw(screen= screen)       