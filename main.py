import pygame as pg
from Config import *
from Scenes import MainGame

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(GAME_NAME)

#Initialization methods
pg.init()
clock = pg.time.Clock()

#Scenes
mainGame = MainGame.MainGame()

#Game Loop
while GAME_STATE:
    
    for event in pg.event.get():
        
        if event.type == pg.QUIT:
            GAME_STATE = False

        elif event.type == pg.KEYDOWN:
            
            if event.key == pg.K_ESCAPE:
                GAME_STATE = False
                
    if SCENE == 'START_MENU':
        pass
    
    elif SCENE == 'MAIN_GAME':
        mainGame.run(screen= screen)
        
    pg.display.flip()
    clock.tick(FPS)    
        
pg.quit()        