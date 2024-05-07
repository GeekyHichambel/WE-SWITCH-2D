import pygame as pg
from Config import *
from Scenes import MainGame
#TODO: Player cap not visible in animation or movement.
#TODO: Map creation with differnet assets and obstacles.

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),pg.FULLSCREEN)
pg.display.set_caption(GAME_NAME)

#Initialization methods
pg.init()
clock = pg.time.Clock()

#Scenes
mainGame = MainGame.MainGame()

#Game Loop
while GAME_STATE:
                
    if SCENE == 'START_MENU':
        pass
    
    elif SCENE == 'MAIN_GAME':
        mainGame.run(screen= screen)
        
    pg.display.flip()
    clock.tick(FPS)    
        
pg.quit()        