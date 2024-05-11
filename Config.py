import pygame as pg

#Constants

#GAME SETUP SETTINGS
GAME_NAME = 'WE-SWITCH 2D'
SCREEN_WIDTH, SCREEN_HEIGHT = 1600,900
FPS = 60

#PATHS
IMAGE_PATH = 'Assets/images/'
SPRITE_PATH = 'Assets/sprites/'
SOUND_PATH = 'Assets/sounds/'
TILE_PATH = 'Assets/sprites/tiles/'
PIPELINE_SET_PATH = 'Assets/sprites/tiles/pipeline/'
MAP_PATH = 'Assets/map/'

#PLAYER CONFIG
PLAYER_SIZE = 800
PLAYER_PIXEL_SIZE = 100
PLAYER_RUN_SPEED = 0.2
IDLE_DELAY = 2
GRAVITY = 15

#TILE CONFIG

#30-pipe-curve-top-left
#1-pipeline-horizontal
#4-pipe-curve-top-right
#24-pipe-corner-bottom
#26-pipe-corner-up
#28-pipe-curve-bottom-left
#29-pipe-curve-bottom-right
TILE_SIZE = SCREEN_HEIGHT//10
PIPELINE_CURVE_TILE_TL = pg.image.load(PIPELINE_SET_PATH + 'pipeline_curve_tl.png')
PIPELINE_CURVE_TILE_TR = pg.image.load(PIPELINE_SET_PATH + 'pipeline_curve_tr.png')
PIPELINE_CURVE_TILE_BL = pg.image.load(PIPELINE_SET_PATH + 'pipeline_curve_bl.png')
PIPELINE_CURVE_TILE_BR = pg.image.load(PIPELINE_SET_PATH + 'pipeline_curve_br.png')
PIPELINE_CORNER_TILE_L = pg.image.load(PIPELINE_SET_PATH + 'pipeline_corner_left.png')
PIPELINE_CORNER_TILE_R = pg.image.load(PIPELINE_SET_PATH + 'pipeline_corner_right.png')
PIPELINE_CORNER_TILE_U = pg.image.load(PIPELINE_SET_PATH + 'pipeline_corner_up.png')
PIPELINE_CORNER_TILE_D = pg.image.load(PIPELINE_SET_PATH + 'pipeline_corner_down.png')
PIPELINE_HORIZONTAL = pg.image.load(PIPELINE_SET_PATH + 'pipeline_horizontal.png')
GOAL_TILE = pg.image.load(TILE_PATH + 'goal.png')

#Global Variables

#GAME SETUP SETTINGS  
gAME_STATE = True
iS_FULLSCREEN = False
sCENE = 'MAIN_GAME'

#PLAYER CONTROLS
PLAYER1_KEY = pg.K_f
PLAYER2_KEY = pg.K_j
FULLSCREEN_KEY = pg.K_BACKSPACE
QUIT_KEY = pg.K_ESCAPE