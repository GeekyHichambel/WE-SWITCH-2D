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
        keys = pg.key.get_pressed()
        
        if keys[PLAYER1_KEY]:
            self.player1.move(action= 'FLIP')
            
        if keys[PLAYER2_KEY]:
            self.player2.move(action= 'FLIP')
            
        self.player1.update()
        self.player2.update()

    def run(self, screen):
        self.update()
        self.draw(screen= screen)       