import pygame, sys, time, os, random, math, colorsys
from pygame.locals import *
from random import *
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

dir = os.path.dirname(__file__)

windowWidth  = 1280
windowHeight = 720
Surface      = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Music Maker')

def text_objects(Text, font, colour):
     textSurface = font.render(Text, True, colour)
     return textSurface, textSurface.get_rect()

def Text(Text, xPos, yPos, Size, Colour):
     largeText          = pygame.font.Font('Fonts/Times_New_Roman_Normal.ttf', Size)
     TextSurf, TextRect = text_objects(Text, largeText, Colour)
     TextRect.center    = (xPos, yPos)

     Surface.blit(TextSurf, TextRect)

#Colors
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
LightGrey2 = (100, 100, 100)
LightGrey2 = (110, 110, 110)
LightGrey3 = (80 , 80 , 80 )
DarkGrey   = (50 , 50 , 50 )

#Piano Tiles Lists
pianoTilesA = []
pianoTilesS = []
pianoTilesD = []
pianoTilesF = []
pianoTilesG = []
pianoTilesH = []
pianoTilesJ = []
pianoTilesK = []
pianoTilesL = []
pianoTilesSEMI = []

pianoTilesW = []
pianoTilesE = []
pianoTilesT = []
pianoTilesY = []
pianoTilesU = []
pianoTilesO = []
pianoTilesP = []

#Other Variables
noteButtonList  = ["", ";", "L", "K", "J", "H", "G", "F", "D", "S", "A"]
keyboardIdle = True

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
        pygame.draw.rect(Surface, Black, (0, 0, windowWidth/3.55, windowHeight/1.75+100), 3)
        pygame.draw.rect(Surface, Black, (0, windowHeight/1.75+100, windowWidth/3.55, windowHeight), 3)
        pygame.draw.rect(Surface, Black, (windowWidth, windowHeight/2, windowWidth/3.55, windowHeight), 3)
        pygame.draw.line(Surface, Black, (0, 35), (400, 35), 4)
        pygame.draw.line(Surface, Black, (0, windowHeight-248), (360, windowHeight-248), 4)
        Text("Recordings", 72, 16, 28, Black)
        Text("Instruments", 77, windowHeight-248+20, 28, Black)
        for x in range(1, 10):
            pygame.draw.line(Surface, Grey2, (windowWidth-(92*x)-3, 0), (windowWidth-(92*x)-3, windowHeight-247), 3)
        pygame.draw.line(Surface, Grey3, (windowWidth-(92*3)-3, 0), (windowWidth-(92*3)-3, windowHeight-247), 3)
        pygame.draw.line(Surface, Grey3, (windowWidth-(92*7)-3, 0), (windowWidth-(92*7)-3, windowHeight-247), 3)

     def RecordButton(record):
          if (record == False):
               pygame.draw.rect(Surface, Grey2, (windowWidth-459-14, 9, 20, 20))
               pygame.draw.rect(Surface, Green  , (windowWidth-459-14, 9, 20, 20), 1)
               Text("•", windowWidth-449-14, 19, 35, Green)
          else:
               pygame.draw.rect(Surface, Grey2, (windowWidth-459-14, 9, 20, 20))
               pygame.draw.rect(Surface, Red, (windowWidth-459-14, 9, 20, 20), 1)
               Text("•", windowWidth-449-14, 19, 35, Red)

     def TopBar():
        pygame.draw.rect(Surface, (150, 150, 150), (windowWidth-918, 2, 918, 35))
        pygame.draw.rect(Surface, Black, (windowWidth-920, 0, 919, 37), 2)

     def WhiteKeyText(buttonList):
        for i in range(1, 12):
            Text(buttonList[i], windowWidth-(92*i)+11, windowHeight-15, 20, Black)
            if i > 9:
                break

     def Icon(iButtonPressed, qButtonPressed):
          if (iButtonPressed):
               pygame.draw.rect(Surface, DarkSkyBlue, (windowWidth-30, 9, 20, 20))
          else:
               pygame.draw.rect(Surface, SkyBlue, (windowWidth-30, 9, 20, 20))
          pygame.draw.rect(Surface, Black, (windowWidth-30, 9, 20, 20), 1)
          Text("I", windowWidth-20, 19, 18, Black)

          if (qButtonPressed):
               pygame.draw.rect(Surface, DarkSkyBlue, (windowWidth-906, 9, 20, 20))
          else:
               pygame.draw.rect(Surface, SkyBlue, (windowWidth-906, 9, 20, 20))
          pygame.draw.rect(Surface, Black, (windowWidth-906, 9, 20, 20), 1)
          Text("O", windowWidth-895, 19, 15, Black)

     def BlackKeyText(buttonList):
        Text("P", windowWidth-104, windowHeight-112, 15, buttonList[0])
        Text("O", windowWidth-196, windowHeight-112, 15, buttonList[1])
        Text("U", windowWidth-380, windowHeight-112, 15, buttonList[2])
        Text("Y", windowWidth-472, windowHeight-112, 15, buttonList[3])
        Text("T", windowWidth-564, windowHeight-112, 15, buttonList[4])
        Text("E", windowWidth-748, windowHeight-112, 15, buttonList[5])
        Text("W", windowWidth-840, windowHeight-112, 15, buttonList[6])

     def VolumeSlider(volumeSliderX, activeSlider):
          pygame.draw.rect(Surface, DarkGrey, (windowWidth-875+35, 16, 100, 5))
          pygame.draw.rect(Surface, Green, (windowWidth-875+35, 16, volumeSliderX, 5))
          pygame.draw.rect(Surface, (230, 230, 230), ((windowWidth-880+35)+volumeSliderX, 11, 10, 15))

          if (activeSlider == False):
               pygame.draw.rect(Surface, Black, (windowWidth-910+35, 8, 20, 20), 2)
               Text("V", windowWidth-900+35, 19, 15, Black)
          elif (activeSlider == True):
               pygame.draw.rect(Surface, Green, (windowWidth-910+35, 8, 20, 20), 2)
               Text("V", windowWidth-900+35, 19, 15, Green)

     def ReverbSlider(reverbSliderX, activeSlider2):
          pygame.draw.rect(Surface, DarkGrey, (windowWidth-725+35, 16, 100, 5))
          pygame.draw.rect(Surface, Green, (windowWidth-725+35, 16, reverbSliderX, 5))
          pygame.draw.rect(Surface, (230, 230, 230), ((windowWidth-730+35)+reverbSliderX, 11, 10, 15))

          if (activeSlider2 == False):
               pygame.draw.rect(Surface, Black, (windowWidth-760+35, 8, 20, 20), 2)
               Text("R", windowWidth-748.5+35, 18, 15, Black)
          elif (activeSlider2 == True):
               pygame.draw.rect(Surface, Green, (windowWidth-760+35, 8, 20, 20), 2)
               Text("R", windowWidth-748.5+35, 18, 15, Green)

     def PianoButton(instruments):
          if (instruments[0] == True):
               pygame.draw.rect(Surface, Black, (10, 520, 100, 50), 2)
               Text("Piano", 55, 545, 30, Black)
               Text("1", 105, 560, 15, Black)
          else:
               pygame.draw.rect(Surface, Grey3, (10, 520, 100, 50), 2)
               Text("Piano", 55, 545, 30, Grey3)
               Text("1", 105, 560, 15, Grey3)

     def BassButton(instruments):
          if (instruments[1] == True):
               pygame.draw.rect(Surface, Black, (10, 570, 100, 50), 2)
               Text("Bass", 46, 595, 30, Black)
               Text("2", 103, 610, 15, Black)
          else:
               pygame.draw.rect(Surface, Grey3, (10, 570, 100, 50), 2)
               Text("Bass", 46, 595, 30, Grey3)
               Text("2", 103, 610, 15, Grey3)

     def InfoWindowText(infoWindowX):
          Text("Press Q to open OCTAVE WINDOW", infoWindowX + 240, 75, 27, Black)
          Text("Press I to open INFO WINDOW", infoWindowX + 211, 110, 27, Black)
          Text("Press R to RECORD", infoWindowX + 141, 145, 27, Black)
          Text("Change instruments in bottom left", infoWindowX + 215, 180, 27, Black)
          Text("Change recordings in top left", infoWindowX + 185, 215, 27, Black)

     def OctaveWindowText(octaveWindowHeight, octave):
          Text("Press Z to lower octave", windowWidth/2.45, octaveWindowHeight - 200, 27, Black)
          Text("Press X to raise octave", windowWidth/2.46, octaveWindowHeight - 140, 27, Black)
          Text("Current octave is " + str(octave), windowWidth/2.57, octaveWindowHeight - 80, 27, Black)
     def recordingBox(yPos):
          pygame.draw.rect(Surface, Grey3, (10, yPos, 337, 95))
          pygame.draw.rect(Surface, Black, (9, yPos-1, 339, 97), 2)

class Function():
     def ChangeVolume(sound, volume):
          sound.set_volume(volume)

#Piano Variables
A1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/A1.wav'))
B1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/B1.wav'))
C1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/C1.wav'))
D1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/D1.wav'))
E1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/E1.wav'))
F1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/F1.wav'))
G1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/G1.wav'))
CSharp1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/CSharp1.wav'))
DSharp1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/DSharp1.wav'))
FSharp1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/FSharp1.wav'))
GSharp1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/GSharp1.wav'))
ASharp1 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/ASharp1.wav'))
          
A2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/A2.wav'))
B2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/B2.wav'))
C2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/C2.wav'))
D2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/D2.wav'))
E2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/E2.wav'))
F2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/F2.wav'))
G2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/G2.wav'))
CSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/CSharp2.wav'))
DSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/DSharp2.wav'))
FSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/FSharp2.wav'))
GSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/GSharp2.wav'))
ASharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/ASharp2.wav'))

A3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/A3.wav'))
B3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/B3.wav'))
C3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/C3.wav'))
D3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/D3.wav'))
E3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/E3.wav'))
F3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/F3.wav'))
G3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/G3.wav'))
CSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/CSharp3.wav'))
DSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/DSharp3.wav'))
FSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/FSharp3.wav'))
GSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/GSharp3.wav'))
ASharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/ASharp3.wav'))

C4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/C4.wav'))
D4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/D4.wav'))
E4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/E4.wav'))
CSharp4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/CSharp4.wav'))
DSharp4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/DSharp4.wav'))

#Bass Variables
#bassA2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/A2.wav'))
#bassB2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/B2.wav'))
#bassC2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/C2.wav'))
#bassD2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/D2.wav'))
#bassE2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/E2.wav'))
#bassF2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/F2.wav'))
#bassG2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/G2.wav'))
#bassCSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/C#2.wav'))
#bassDSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/D#2.wav'))
#bassFSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/F#2.wav'))
#bassGSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/G#2.wav'))
#bassASharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/A#2.wav'))
