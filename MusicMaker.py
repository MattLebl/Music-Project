#Current Known Bugs:
#When switching octives while pressing a note, then releasing it in the new octive, the old octive note will not fade out

import pygame, sys, time, os, random, math, colorsys
from pygame.locals import *
from random import *
<<<<<<< HEAD
#from ctypes import windll, Structure, c_long, byref
=======
>>>>>>> 8ce16b7ee5887375201317c1f4c8874f05e55516

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

FPS=30
fpsClock=pygame.time.Clock()

dir = os.path.dirname(__file__)

#Music Code
#[Variable] = pygame.mixer.Sound(FileLocation)
#[Variable].play()
#[Variable].stop()
#[Variable].fadeout() This will stop playback of the sound after fading out over the time argument in milliseconds.
#[Variable].get_length() Return the length of this Sound in seconds
#[Variable].set_volume()
#[Variable].get_volume()
#https://www.pygame.org/docs/ref/mixer.html

#Window Variables
windowWidth  = 1280
windowHeight = 720

#Sound Variables
<<<<<<< HEAD
A2 = pygame.mixer.Sound(os.path.join(dir, './A2.wav'))
B2 = pygame.mixer.Sound(os.path.join(dir, './B2.wav'))
C2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/C2.wav'))
D2 = pygame.mixer.Sound(os.path.join(dir, './D2.wav'))
E2 = pygame.mixer.Sound(os.path.join(dir, './E2.wav'))
F2 = pygame.mixer.Sound(os.path.join(dir, './F2.wav'))
G2 = pygame.mixer.Sound(os.path.join(dir, './G2.wav'))

C3 = pygame.mixer.Sound(os.path.join(dir, './C3.wav'))
D3 = pygame.mixer.Sound(os.path.join(dir, './D3.wav'))
E3 = pygame.mixer.Sound(os.path.join(dir, './E3.wav'))
=======
A2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/A2.wav'))
B2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/B2.wav'))
C2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/C2.wav'))
D2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/D2.wav'))
E2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/E2.wav'))
F2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/F2.wav'))
G2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/G2.wav'))
CSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/CSharp2.wav'))
DSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/DSharp2.wav'))
FSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/FSharp2.wav'))
GSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/GSharp2.wav'))
ASharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/ASharp2.wav'))

A3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/A3.wav'))
B3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/B3.wav'))
C3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/C3.wav'))
D3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/D3.wav'))
E3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/E3.wav'))
F3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/F3.wav'))
G3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/G3.wav'))
CSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/CSharp3.wav'))
DSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/DSharp3.wav'))
FSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/FSharp3.wav'))
GSharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/GSharp3.wav'))
ASharp3 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/ASharp3.wav'))

C4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/C4.wav'))
D4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/D4.wav'))
E4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/E4.wav'))
CSharp4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/CSharp4.wav'))
DSharp4 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/DSharp4.wav'))
>>>>>>> 8ce16b7ee5887375201317c1f4c8874f05e55516

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
Grey       = (60 , 60 , 60 )
Grey2      = (65 , 65 , 65 )
Grey3      = (75 , 75 , 75 )
LightGrey  = (125, 125, 125)
DarkGrey   = (50 , 50 , 50 )

blackNoteKeys = []
for x in range(0, 8):
    blackNoteKeys.append((255, 255, 255))

#Lists
noteColorsWhite = []
for i in range(0, 10):
    noteColorsWhite.append((255, 255, 255))
noteColorsBlack = []
for i in range(0, 7):
    noteColorsBlack.append((0  , 0  , 0  ))
noteButtonList  = ["", ";", "L", "K", "J", "H", "G", "F", "D", "S", "A"]
currentOctive   = [False, True, False]

#Paino Tiles Lists
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

#Set up the window
Surface    = pygame.display.set_mode((windowWidth, windowHeight))
fadeScreen = pygame.Surface((windowWidth, windowHeight))
pygame.display.set_caption('Music Maker')

#Variables
volumeSliderX = 50
volume = 1
activeSlider = False;

#Mouse Variables
mousePosition = pygame.mouse.get_pos()
mousePressed  = pygame.mouse.get_pressed()

#Def Functions
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

def ChangeVolume(sound):
    sound.set_volume(volume)

#Text Functions
def text_objects(Text, font, colour):
     textSurface = font.render(Text, True, colour)
     return textSurface, textSurface.get_rect()

def Text(Text, xPos, yPos, Size, Colour):
     largeText          = pygame.font.Font('Fonts/Times_New_Roman_Normal.ttf', Size)
     TextSurf, TextRect = text_objects(Text, largeText, Colour)
     TextRect.center    = (xPos, yPos)

     Surface.blit(TextSurf, TextRect)

while True: #Game Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            #Notes Pressed

            #Moves Octive down
            if (event.key == K_z):
                if (currentOctive[1] == True):
                    currentOctive[1] = False
                    currentOctive[0] = True
                if (currentOctive[2] == True):
                    currentOctive[2] = False
                    currentOctive[1] = True

            #Moves Octive up
            if (event.key == K_x):
                if (currentOctive[1] == True):
                    currentOctive[1] = False
                    currentOctive[2] = True
                if (currentOctive[0] == True):
                    currentOctive[0] = False
                    currentOctive[1] = True

            #Resets octive to base
            if (event.key == K_c):
                currentOctive[1] = True
                currentOctive[0] = False
                currentOctive[2] = False
            
            if (event.key == K_a):
                noteColorsWhite[0] = (0, 255, 0)
                pianoTilesA.append([windowWidth-920, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    C2.play()
                elif (currentOctive[2] == True):
                    C3.play()
            if (event.key == K_s):
                noteColorsWhite[1] = (0, 255, 0)
                pianoTilesS.append([windowWidth-828, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    D2.play()
                elif (currentOctive[2] == True):
                    D3.play()
            if (event.key == K_d):
                noteColorsWhite[2] = (0, 255, 0)
                pianoTilesD.append([windowWidth-736, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    E2.play()
                elif (currentOctive[2] == True):
                    E3.play()
            if (event.key == K_f):
                noteColorsWhite[3] = (0, 255, 0)
                pianoTilesF.append([windowWidth-644, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    F2.play()
                elif (currentOctive[2] == True):
                    F3.play()
            if (event.key == K_g):
                noteColorsWhite[4] = (0, 255, 0)
                pianoTilesG.append([windowWidth-552, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    G2.play()
                elif (currentOctive[2] == True):
                    G3.play()
            if (event.key == K_h):
                noteColorsWhite[5] = (0, 255, 0)
                pianoTilesH.append([windowWidth-460, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    A2.play()
                elif (currentOctive[2] == True):
                    A3.play()
            if (event.key == K_j):
                noteColorsWhite[6] = (0, 255, 0)
                pianoTilesJ.append([windowWidth-368, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    B2.play()
                elif (currentOctive[2] == True):
                    B3.play()
            if (event.key == K_k):
                noteColorsWhite[7] = (0, 255, 0)
                pianoTilesK.append([windowWidth-276, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    C3.play()
                elif (currentOctive[2] == True):
                    C4.play()
            if (event.key == K_l):
                noteColorsWhite[8] = (0, 255, 0)
                pianoTilesL.append([windowWidth-184, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    D3.play()
                elif (currentOctive[2] == True):
                    D4.play()
            if (event.key == K_SEMICOLON):
                noteColorsWhite[9] = (0, 255, 0)
                pianoTilesSEMI.append([windowWidth-92, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    E3.play()
                elif (currentOctive[2] == True):
                    E4.play()

            if (event.key == K_w):
                noteColorsBlack[0] = (0  , 150, 0  )
                blackNoteKeys[6]   = (0, 0, 0)
                pianoTilesW.append([windowWidth-853, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    CSharp2.play()
                elif (currentOctive[2] == True):
                    CSharp3.play()
            if (event.key == K_e):
                noteColorsBlack[1] = (0  , 150, 0  )
                blackNoteKeys[5]   = (0, 0, 0)
                pianoTilesE.append([windowWidth-761, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    DSharp2.play()
                elif (currentOctive[2] == True):
                    DSharp3.play()
            if (event.key == K_t):
                noteColorsBlack[2] = (0  , 150, 0  )
                blackNoteKeys[4]   = (0, 0, 0)
                pianoTilesT.append([windowWidth-577, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    FSharp2.play()
                elif (currentOctive[2] == True):
                    FSharp3.play()
            if (event.key == K_y):
                noteColorsBlack[3] = (0  , 150, 0  )
                blackNoteKeys[3]   = (0, 0, 0)
                pianoTilesY.append([windowWidth-484, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    GSharp2.play()
                elif (currentOctive[2] == True):
                    GSharp3.play()
            if (event.key == K_u):
                noteColorsBlack[4] = (0  , 150, 0  )
                blackNoteKeys[2]   = (0, 0, 0)
                pianoTilesU.append([windowWidth-392, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    ASharp2.play()
                elif (currentOctive[2] == True):
                    ASharp3.play()
            if (event.key == K_o):
                noteColorsBlack[5] = (0  , 150, 0  )
                blackNoteKeys[1]   = (0, 0, 0)
                pianoTilesO.append([windowWidth-208, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    CSharp3.play()
                elif (currentOctive[2] == True):
                    CSharp4.play()
            if (event.key == K_p):
                noteColorsBlack[6] = (0  , 150, 0  )
                blackNoteKeys[0]   = (0, 0, 0)
                pianoTilesP.append([windowWidth-116, windowHeight-247, 0, True])
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    DSharp3.play()
                elif (currentOctive[2] == True):
                    DSharp4.play()
            
        if event.type == KEYUP:
            #Notes Released
            if (event.key == K_a):
                noteColorsWhite[0] = (255, 255, 255)
                pianoTilesA[len(pianoTilesA)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    C2.fadeout(500)
                elif (currentOctive[2] == True):
                    C3.fadeout(500)
            if (event.key == K_s):
                noteColorsWhite[1] = (255, 255, 255)
                pianoTilesS[len(pianoTilesS)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    D2.fadeout(500)
                elif (currentOctive[2] == True):
                    D3.fadeout(500)
            if (event.key == K_d):
                noteColorsWhite[2] = (255, 255, 255)
                pianoTilesD[len(pianoTilesD)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    E2.fadeout(500)
                elif (currentOctive[2] == True):
                    E3.fadeout(500)
            if (event.key == K_f):
                noteColorsWhite[3] = (255, 255, 255)
                pianoTilesF[len(pianoTilesF)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    F2.fadeout(500)
                elif (currentOctive[2] == True):
                    F3.fadeout(500)
            if (event.key == K_g):
                noteColorsWhite[4] = (255, 255, 255)
                pianoTilesG[len(pianoTilesG)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    G2.fadeout(500)
                elif (currentOctive[2] == True):
                    G3.fadeout(500)
            if (event.key == K_h):
                noteColorsWhite[5] = (255, 255, 255)
                pianoTilesH[len(pianoTilesH)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    A2.fadeout(500)
                elif (currentOctive[2] == True):
                    A3.fadeout(500)
            if (event.key == K_j):
                noteColorsWhite[6] = (255, 255, 255)
                pianoTilesJ[len(pianoTilesJ)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    B2.fadeout(500)
                elif (currentOctive[2] == True):
                    B3.fadeout(500)
            if (event.key == K_k):
                noteColorsWhite[7] = (255, 255, 255)
                pianoTilesK[len(pianoTilesK)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    C3.fadeout(500)
                elif (currentOctive[2] == True):
                    C4.fadeout(500)
            if (event.key == K_l):
                noteColorsWhite[8] = (255, 255, 255)
                pianoTilesL[len(pianoTilesL)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    D3.fadeout(500)
                elif (currentOctive[2] == True):
                    D4.fadeout(500)
            if (event.key == K_SEMICOLON):
                noteColorsWhite[9] = (255, 255, 255)
                pianoTilesSEMI[len(pianoTilesSEMI)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    E3.fadeout(500)
                elif (currentOctive[2] == True):
                    E4.fadeout(500)
                
            if (event.key == K_w):
                noteColorsBlack[0] = (0, 0, 0)
                blackNoteKeys[6]   = (255, 255, 255)
                pianoTilesW[len(pianoTilesW)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    CSharp2.fadeout(500)
                elif (currentOctive[2] == True):
                    CSharp3.fadeout(500)
            if (event.key == K_e):
                noteColorsBlack[1] = (0, 0, 0)
                blackNoteKeys[5]   = (255, 255, 255)
                pianoTilesE[len(pianoTilesE)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    DSharp2.fadeout(500)
                elif (currentOctive[2] == True):
                    DSharp3.fadeout(500)
            if (event.key == K_t):
                noteColorsBlack[2] = (0, 0, 0)
                blackNoteKeys[4]   = (255, 255, 255)
                pianoTilesT[len(pianoTilesT)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    FSharp2.fadeout(500)
                elif (currentOctive[2] == True):
                    FSharp3.fadeout(500)
            if (event.key == K_y):
                noteColorsBlack[3] = (0, 0, 0)
                blackNoteKeys[3]   = (255, 255, 255)
                pianoTilesY[len(pianoTilesY)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    GSharp2.fadeout(500)
                elif (currentOctive[2] == True):
                    GSharp3.fadeout(500)
            if (event.key == K_u):
                noteColorsBlack[4] = (0, 0, 0)
                blackNoteKeys[2]   = (255, 255, 255)
                pianoTilesU[len(pianoTilesU)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    ASharp2.fadeout(500)
                elif (currentOctive[2] == True):
                    ASharp3.fadeout(500)
            if (event.key == K_o):
                noteColorsBlack[5] = (0, 0, 0)
                blackNoteKeys[1]   = (255, 255, 255)
                pianoTilesO[len(pianoTilesO)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    CSharp3.fadeout(500)
                elif (currentOctive[2] == True):
                    CSharp4.fadeout(400)
            if (event.key == K_p):
                noteColorsBlack[6] = (0, 0, 0)
                blackNoteKeys[0]   = (255, 255, 255)
                pianoTilesP[len(pianoTilesP)-1][3] = False
                if (currentOctive[0] == True):
                    print("First Octive Note")
                elif (currentOctive[1] == True):
                    DSharp3.fadeout(500)
                elif (currentOctive[2] == True):
                    DSharp4.fadeout(500)
    
    #Change Volume
    volume = volumeSliderX/50
    ChangeVolume(A2)
    ChangeVolume(B2)
    ChangeVolume(C2)
    ChangeVolume(D2)
    ChangeVolume(E2)
    ChangeVolume(F2)
    ChangeVolume(G2)
    ChangeVolume(CSharp2)
    ChangeVolume(DSharp2)
    ChangeVolume(FSharp2)
    ChangeVolume(GSharp2)
    ChangeVolume(ASharp2)
    ChangeVolume(C3)
    ChangeVolume(D3)
    ChangeVolume(E3)
    ChangeVolume(CSharp3)
    ChangeVolume(DSharp3)

    #Move Bar
    mousePressed = pygame.mouse.get_pressed()
    mousePosition = pygame.mouse.get_pos()
    
    if (mousePressed[0] == 1 and mousePosition[0] <= (windowWidth-905)+volumeSliderX+10 and mousePosition[0] >= (windowWidth-905)+volumeSliderX and mousePosition[1] >= 11 and mousePosition[1] <= 26):
        activeSlider = True;

    if (activeSlider):
        volumeSliderX = mousePosition[0]-380
        if (mousePressed[0] == 0):
            activeSlider = False;

    if (volumeSliderX > 100):
        volumeSliderX = 100
    elif (volumeSliderX < 0):
        volumeSliderX = 0

    #Background
    pygame.draw.rect(Surface, LightGrey, (0, 0, windowWidth, windowHeight))
    pygame.draw.rect(Surface, Grey, (windowWidth-920, 0, 920, windowHeight))
    pygame.draw.line(Surface, Black, (windowWidth-922, windowHeight), (windowWidth-922, 0), 5)
    for x in range(1, 10):
        pygame.draw.line(Surface, Grey2, (windowWidth-(92*x)-3, 0), (windowWidth-(92*x)-3, windowHeight-247), 3)
    pygame.draw.line(Surface, Grey3, (windowWidth-(92*3)-3, 0), (windowWidth-(92*3)-3, windowHeight-247), 3)
    pygame.draw.line(Surface, Grey3, (windowWidth-(92*7)-3, 0), (windowWidth-(92*7)-3, windowHeight-247), 3)

    #Delete Tiles
    DeleteTiles(pianoTilesA)
    DeleteTiles(pianoTilesS)
    DeleteTiles(pianoTilesD)
    DeleteTiles(pianoTilesF)
    DeleteTiles(pianoTilesG)
    DeleteTiles(pianoTilesH)
    DeleteTiles(pianoTilesJ)
    DeleteTiles(pianoTilesK)
    DeleteTiles(pianoTilesL)
    DeleteTiles(pianoTilesSEMI)
    DeleteTiles(pianoTilesW)
    DeleteTiles(pianoTilesE)
    DeleteTiles(pianoTilesT)
    DeleteTiles(pianoTilesY)
    DeleteTiles(pianoTilesU)
    DeleteTiles(pianoTilesO)
    DeleteTiles(pianoTilesP)

    #Move Tiles
    MoveTiles(pianoTilesA)
    MoveTiles(pianoTilesS)
    MoveTiles(pianoTilesD)
    MoveTiles(pianoTilesF)
    MoveTiles(pianoTilesG)
    MoveTiles(pianoTilesH)
    MoveTiles(pianoTilesJ)
    MoveTiles(pianoTilesK)
    MoveTiles(pianoTilesL)
    MoveTiles(pianoTilesSEMI)
    MoveTiles(pianoTilesW)
    MoveTiles(pianoTilesE)
    MoveTiles(pianoTilesT)
    MoveTiles(pianoTilesY)
    MoveTiles(pianoTilesU)
    MoveTiles(pianoTilesO)
    MoveTiles(pianoTilesP)

    #Draw Tiles
    DrawTiles(pianoTilesA)
    DrawTiles(pianoTilesS)
    DrawTiles(pianoTilesD)
    DrawTiles(pianoTilesF)
    DrawTiles(pianoTilesG)
    DrawTiles(pianoTilesH)
    DrawTiles(pianoTilesJ)
    DrawTiles(pianoTilesK)
    DrawTiles(pianoTilesL)
    DrawTiles(pianoTilesSEMI)
    DrawBlackTiles(pianoTilesW)
    DrawBlackTiles(pianoTilesE)
    DrawBlackTiles(pianoTilesT)
    DrawBlackTiles(pianoTilesY)
    DrawBlackTiles(pianoTilesU)
    DrawBlackTiles(pianoTilesO)
    DrawBlackTiles(pianoTilesP)

    #Draw Piano
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

    #White Key Text
    for i in range(1, 12):
        Text(noteButtonList[i], windowWidth-(92*i)+11, windowHeight-15, 20, Black)
        if i > 9:
            break
    
    #Black Key Text
    Text("P", windowWidth-104, windowHeight-112, 15, blackNoteKeys[0])
    Text("O", windowWidth-196, windowHeight-112, 15, blackNoteKeys[1])
    Text("U", windowWidth-380, windowHeight-112, 15, blackNoteKeys[2])
    Text("Y", windowWidth-472, windowHeight-112, 15, blackNoteKeys[3])
    Text("T", windowWidth-564, windowHeight-112, 15, blackNoteKeys[4])
    Text("E", windowWidth-748, windowHeight-112, 15, blackNoteKeys[5])
    Text("W", windowWidth-840, windowHeight-112, 15, blackNoteKeys[6])

    #Top Bar
    pygame.draw.rect(Surface, (150, 150, 150), (windowWidth-918, 2, 918, 35))
    pygame.draw.rect(Surface, Black, (windowWidth-920, 0, 919, 37), 2)

    pygame.draw.rect(Surface, DarkGrey, (windowWidth-900, 16, 100, 5))
    pygame.draw.rect(Surface, Green, (windowWidth-900, 16, volumeSliderX, 5))
    pygame.draw.rect(Surface, (230, 230, 230), ((windowWidth-905)+volumeSliderX, 11, 10, 15))
    
    pygame.display.flip()
    fpsClock.tick(FPS)
