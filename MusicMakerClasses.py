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

def text_objects(Text, font, colour):
     textSurface = font.render(Text, True, colour)
     return textSurface, textSurface.get_rect()

def Text(Text, xPos, yPos, Size, Colour):
     largeText          = pygame.font.Font('Fonts/Times_New_Roman_Normal.ttf', Size)
     TextSurf, TextRect = text_objects(Text, largeText, Colour)
     TextRect.center    = (xPos, yPos)

     Surface.blit(TextSurf, TextRect)

class Mouse():
    def Position():
        p = pygame.mouse.get_pos()

        return p

    def Pressed():
        p = pygame.mouse.get_pressed()

        return p

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

     def Background():
        pygame.draw.rect(Surface, LightGrey, (0, 0, windowWidth, windowHeight))
        pygame.draw.rect(Surface, Grey, (windowWidth-920, 0, 920, windowHeight))
        pygame.draw.line(Surface, Black, (windowWidth-922, windowHeight), (windowWidth-922, 0), 5)
        pygame.draw.rect(Surface, Black, (0, 0, windowWidth/3.55, windowHeight/2), 3)
        pygame.draw.rect(Surface, Black, (windowWidth, windowHeight/2, windowWidth/3.55, windowHeight), 3)
        for x in range(1, 10):
            pygame.draw.line(Surface, Grey2, (windowWidth-(92*x)-3, 0), (windowWidth-(92*x)-3, windowHeight-247), 3)
        pygame.draw.line(Surface, Grey3, (windowWidth-(92*3)-3, 0), (windowWidth-(92*3)-3, windowHeight-247), 3)
        pygame.draw.line(Surface, Grey3, (windowWidth-(92*7)-3, 0), (windowWidth-(92*7)-3, windowHeight-247), 3)

     def TopBar():
        pygame.draw.rect(Surface, (150, 150, 150), (windowWidth-918, 2, 918, 35))
        pygame.draw.rect(Surface, Black, (windowWidth-920, 0, 919, 37), 2)

     def WhiteKeyText(buttonList):
        for i in range(1, 12):
            Text(buttonList[i], windowWidth-(92*i)+11, windowHeight-15, 20, Black)
            if i > 9:
                break

     def BlackKeyText(buttonList):
        Text("P", windowWidth-104, windowHeight-112, 15, buttonList[0])
        Text("O", windowWidth-196, windowHeight-112, 15, buttonList[1])
        Text("U", windowWidth-380, windowHeight-112, 15, buttonList[2])
        Text("Y", windowWidth-472, windowHeight-112, 15, buttonList[3])
        Text("T", windowWidth-564, windowHeight-112, 15, buttonList[4])
        Text("E", windowWidth-748, windowHeight-112, 15, buttonList[5])
        Text("W", windowWidth-840, windowHeight-112, 15, buttonList[6])

     def VolumeSlider(volumeSliderX, activeSlider):
          pygame.draw.rect(Surface, DarkGrey, (windowWidth-875, 16, 100, 5))
          pygame.draw.rect(Surface, Green, (windowWidth-875, 16, volumeSliderX, 5))
          pygame.draw.rect(Surface, (230, 230, 230), ((windowWidth-880)+volumeSliderX, 11, 10, 15))

          if (activeSlider == False):
               pygame.draw.rect(Surface, Black, (windowWidth-910, 8, 20, 20), 2)
               Text("V", windowWidth-900, 19, 15, Black)
          elif (activeSlider == True):
               pygame.draw.rect(Surface, Green, (windowWidth-910, 8, 20, 20), 2)
               Text("V", windowWidth-900, 19, 15, Green)

     def ReverbSlider(reverbSliderX, activeSlider2):
          pygame.draw.rect(Surface, DarkGrey, (windowWidth-725, 16, 100, 5))
          pygame.draw.rect(Surface, Green, (windowWidth-725, 16, reverbSliderX, 5))
          pygame.draw.rect(Surface, (230, 230, 230), ((windowWidth-730)+reverbSliderX, 11, 10, 15))

          if (activeSlider2 == False):
               pygame.draw.rect(Surface, Black, (windowWidth-760, 8, 20, 20), 2)
               Text("R", windowWidth-748.5, 18, 15, Black)
          elif (activeSlider2 == True):
               pygame.draw.rect(Surface, Green, (windowWidth-760, 8, 20, 20), 2)
               Text("R", windowWidth-748.5, 18, 15, Green)

class Function():
     def ChangeVolume(sound, volume):
          sound.set_volume(volume)


