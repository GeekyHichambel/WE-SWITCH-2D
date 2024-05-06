import pygame as pg
from Models.Player import player
from Config import *

class MainGame():
    
    def __init__(self):
        self.background = pg.image.load(ASSETS_PATH + 'images/background.png').convert()
        self.background = pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.player = player.Player(100, 100)

    def draw(self, screen):
        screen.blit(self.background, (0,0))
        self.player.draw(screen)
        
    def update(self):
        self.player.update()

    def run(self, screen):
        self.update()
        self.draw(screen= screen)       