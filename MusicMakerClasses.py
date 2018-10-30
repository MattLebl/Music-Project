import pygame, sys, time, os, random, math, colorsys
from pygame.locals import *
from random import *

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

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
SkyBlue    = (135, 200, 255)
DarkSkyBlue= (95 , 160, 215)
Grey       = (60 , 60 , 60 )
Grey2      = (65 , 65 , 65 )
Grey3      = (75 , 75 , 75 )
LightGrey  = (125, 125, 125)
DarkGrey   = (50 , 50 , 50 )

windowWidth  = 1280
windowHeight = 720
Surface    = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Music Maker')

class Draw():
    def WhiteKey(x, y, color):
        pygame.draw.rect(Surface, color, (x, y, 90, 245))
        pygame.draw.rect(Surface, Black, (x-2, y-2, 92, 247), 3)

    def BlackKey(x, y, color):
        pygame.draw.rect(Surface, color, (x, y, 45, (249/2)+20))
        pygame.draw.rect(Surface, Black, (x, y-2, 45, (249/2)+22), 3)

    def DeleteTiles(tileList):
        for t in tileList[:]:
            if t[1]+t[2] <= 0:
                tileList.remove(t)
                break

    def MoveTiles(tileList):
        for t in tileList[:]:
            t[1] -= 8
            if t[3] == True:
                t[2] += 8

    def DrawTiles(tileList):
        for t in tileList[:]:
            pygame.draw.rect(Surface, Green, (t[0], t[1], 90, t[2]-2))
            pygame.draw.rect(Surface, Black, (t[0]-2, t[1]-2, 92, t[2]), 3)

    def DrawBlackTiles(tileList):
        for t in tileList[:]:
            pygame.draw.rect(Surface, DarkGreen, (t[0], t[1], 45, t[2]-2))
            pygame.draw.rect(Surface, Black, (t[0], t[1]-2, 45, t[2]), 3)

class Function():
    def ChangeVolume(sound, volume):
        sound.set_volume(volume)
