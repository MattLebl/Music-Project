import pygame, sys, time, os, random, math, colorsys
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
    pygame.draw.rect(Surface, Black, (x, y-2, 45, (249/2)+22), 3)

while True: #Game Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            #Notes Pressed
            if (event.key == K_a):
                noteColorsWhite[0] = (0, 255, 0)
            if (event.key == K_s):
                noteColorsWhite[1] = (0, 255, 0)
            if (event.key == K_d):
                noteColorsWhite[2] = (0, 255, 0)
            if (event.key == K_f):
                noteColorsWhite[3] = (0, 255, 0)
            if (event.key == K_g):
                noteColorsWhite[4] = (0, 255, 0)
            if (event.key == K_h):
                noteColorsWhite[5] = (0, 255, 0)
            if (event.key == K_j):
                noteColorsWhite[6] = (0, 255, 0)
            if (event.key == K_k):
                noteColorsWhite[7] = (0, 255, 0)
            if (event.key == K_l):
                noteColorsWhite[8] = (0, 255, 0)
            if (event.key == K_SEMICOLON):
                noteColorsWhite[9] = (0, 255, 0)

            if (event.key == K_w):
                noteColorsBlack[0] = (0, 150, 0)
            if (event.key == K_e):
                noteColorsBlack[1] = (0, 150, 0)
            if (event.key == K_t):
                noteColorsBlack[2] = (0, 150, 0)
            if (event.key == K_y):
                noteColorsBlack[3] = (0, 150, 0)
            if (event.key == K_u):
                noteColorsBlack[4] = (0, 150, 0)
            if (event.key == K_o):
                noteColorsBlack[5] = (0, 150, 0)
            if (event.key == K_p):
                noteColorsBlack[6] = (0, 150, 0)
            
        if event.type == KEYUP:
            #Notes Released
            if (event.key == K_a):
                noteColorsWhite[0] = (255, 255, 255)
            if (event.key == K_s):
                noteColorsWhite[1] = (255, 255, 255)
            if (event.key == K_d):
                noteColorsWhite[2] = (255, 255, 255)
            if (event.key == K_f):
                noteColorsWhite[3] = (255, 255, 255)
            if (event.key == K_g):
                noteColorsWhite[4] = (255, 255, 255)
            if (event.key == K_h):
                noteColorsWhite[5] = (255, 255, 255)
            if (event.key == K_j):
                noteColorsWhite[6] = (255, 255, 255)
            if (event.key == K_k):
                noteColorsWhite[7] = (255, 255, 255)
            if (event.key == K_l):
                noteColorsWhite[8] = (255, 255, 255)
            if (event.key == K_SEMICOLON):
                noteColorsWhite[9] = (255, 255, 255)

            if (event.key == K_w):
                noteColorsBlack[0] = (0, 0, 0)
            if (event.key == K_e):
                noteColorsBlack[1] = (0, 0, 0)
            if (event.key == K_t):
                noteColorsBlack[2] = (0, 0, 0)
            if (event.key == K_y):
                noteColorsBlack[3] = (0, 0, 0)
            if (event.key == K_u):
                noteColorsBlack[4] = (0, 0, 0)
            if (event.key == K_o):
                noteColorsBlack[5] = (0, 0, 0)
            if (event.key == K_p):
                noteColorsBlack[6] = (0, 0, 0)


    #Background
    pygame.draw.rect(Surface, LightGrey, (0, 0, windowWidth, windowHeight))
    pygame.draw.rect(Surface, Grey, (windowWidth-920, 0, 920, windowHeight))
    pygame.draw.line(Surface, Black, (windowWidth-922, windowHeight), (windowWidth-922, 0), 5)

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
    
    BlackKey(windowWidth-116, windowHeight-247, noteColorsBlack[6])
    BlackKey(windowWidth-208, windowHeight-247, noteColorsBlack[5])
    BlackKey(windowWidth-392, windowHeight-247, noteColorsBlack[4])
    BlackKey(windowWidth-484, windowHeight-247, noteColorsBlack[3])
    BlackKey(windowWidth-577, windowHeight-247, noteColorsBlack[2])
    BlackKey(windowWidth-761, windowHeight-247, noteColorsBlack[1])
    BlackKey(windowWidth-853, windowHeight-247, noteColorsBlack[0])

    pygame.display.flip()
    fpsClock.tick(FPS)
    
