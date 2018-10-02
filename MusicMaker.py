import pygame, sys, time, os, random, math, colorsys, keyboard
from pygame.locals import *
from random import *
from ctypes import windll, Structure, c_long, byref

pygame.mixer.pre_init(frequency = 22050, size = -16, channels = 2, buffer = 4096)
pygame.mixer.init(frequency = 22050, size = -16, channels = 2, buffer = 4096)

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

#Window Variables
windowWidth  = 1280
windowHeight = 720

#Colour Variables
Black      = (0  , 0  , 0  )
White      = (255, 255, 255)
Red        = (255, 0  , 0  )
LightGreen = (0  , 255, 48 )
Green      = (0  , 255, 0  )
DarkGreen  = (0  , 150, 0  )
Yellow     = (255, 255, 0  )
DarkYellow = (150, 150, 0  )
Orange     = (255, 165, 0  )
DarkOrange = (240, 120, 0  )
Red        = (255, 0  , 0  )
DarkRed    = (150, 0  , 0  )
Blue       = (0  , 0  , 255)
Grey       = (75 , 75 , 75 )
LightGrey  = (125, 125, 125)
DarkGrey   = (50 , 50 , 50 )

#Variables

#Set up the window
Surface    = pygame.display.set_mode((windowWidth, windowHeight))
fadeScreen = pygame.Surface((windowWidth, windowHeight))
pygame.display.set_caption('Music Maker')

#Def Functions
def WhiteKey(x, y, color):
    pygame.draw.rect(Surface, color, (x, y, 100, 245))
    pygame.draw.rect(Surface, Black, (x-3, y-3, 103, 248), 3)

#Extra Notes
#Piano Tiles Length: 1024 Pixels
#Individual Octive Length: 341 Pixels
#White Tile Length: 48 Pixels
#0.323/1.563z

while True: #Game Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(Surface, LightGrey, (0, 0, windowWidth, windowHeight), 0)

    WhiteKey(windowWidth-100, windowHeight-245, White)

    #High Octive
    

    pygame.display.flip()
    fpsClock.tick(FPS)
    
