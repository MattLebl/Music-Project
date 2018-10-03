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

#Lists
noteColorsWhite = [(255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255)]
noteColorsBlack = [(0  , 0  , 0  ), (0  , 0  , 0  ), (0  , 0  , 0  ), (0  , 0  , 0  ), (0  , 0  , 0  ), (0  , 0  , 0  ), (0  , 0  , 0  )]
keys = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';']

#Set up the window
Surface    = pygame.display.set_mode((windowWidth, windowHeight))
fadeScreen = pygame.Surface((windowWidth, windowHeight))
pygame.display.set_caption('Music Maker')

#Def Functions
def WhiteKey(x, y, color):
    pygame.draw.rect(Surface, color, (x, y, 90, 245))
    pygame.draw.rect(Surface, Black, (x-2, y-2, 92, 247), 3)

def BlackKey(x, y, color):
    pygame.draw.rect(Surface, color, (x, y, 45, (249/2)+20))

while True: #Game Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        #Keyboard Inputs
        


    #Background
    pygame.draw.rect(Surface, LightGrey, (0, 0, windowWidth, windowHeight), 0)

    #High Octive
    WhiteKey(windowWidth-92 , windowHeight-247, noteColorsWhite[9])
    WhiteKey(windowWidth-184, windowHeight-247, noteColorsWhite[8])
    WhiteKey(windowWidth-276, windowHeight-247, noteColorsWhite[7])
    WhiteKey(windowWidth-368, windowHeight-247, noteColorsWhite[6])
    WhiteKey(windowWidth-460, windowHeight-247, noteColorsWhite[5])
    WhiteKey(windowWidth-552, windowHeight-247, noteColorsWhite[4])
    WhiteKey(windowWidth-644, windowHeight-247, noteColorsWhite[3])
    WhiteKey(windowWidth-736, windowHeight-247, noteColorsWhite[2])
    WhiteKey(windowWidth-828, windowHeight-247, noteColorsWhite[1])
    WhiteKey(windowWidth-920, windowHeight-247, noteColorsWhite[0])
    
    BlackKey(windowWidth-116, windowHeight-247, Black)
    BlackKey(windowWidth-208, windowHeight-247, Black)
    BlackKey(windowWidth-392, windowHeight-247, Black)
    BlackKey(windowWidth-484, windowHeight-247, Black)
    BlackKey(windowWidth-577, windowHeight-247, Black)
    BlackKey(windowWidth-761, windowHeight-247, Black)
    BlackKey(windowWidth-853, windowHeight-247, Black)

    pygame.display.flip()
    fpsClock.tick(FPS)
    
