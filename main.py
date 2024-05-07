import pygame as pg
import Config as Global
from Scenes import MainGame
#TODO: Player cap not visible in animation or movement.
#TODO: Map creation with differnet assets and obstacles.

screen = pg.display.set_mode((Global.SCREEN_WIDTH, Global.SCREEN_HEIGHT),pg.FULLSCREEN if Global.iS_FULLSCREEN else 0)
pg.display.set_caption(Global.GAME_NAME)


#Initialization methods
pg.init()
clock = pg.time.Clock()

#Scenes
mainGame = MainGame.MainGame()

#Game Loop
while Global.gAME_STATE:
                
    if Global.sCENE == 'START_MENU':
        pass
    
    elif Global.sCENE == 'MAIN_GAME':
        mainGame.run(screen= screen)
        
    pg.display.flip()
    clock.tick(Global.FPS)    
        
pg.quit()        