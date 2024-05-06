import pygame as pg
from Config import *

class MainGame():
    
    def __init__(self):
        self.background = pg.image.load(ASSETS_PATH + 'images/background.png').convert()
        self.background = pg.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self, screen):
        screen.blit(self.background, (0,0))