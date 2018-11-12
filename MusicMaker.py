#https://stackoverflow.com/questions/9770073/sound-generation-synthesis-with-python
#https://soledadpenades.com/posts/2009/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/

from MusicMakerClasses import *

FPS=30
fpsClock=pygame.time.Clock()

dir = os.path.dirname(__file__)

#Window Variables
windowWidth  = 1280
windowHeight = 720

#Sound Variables
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

#Bass
bassA2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Bass/A2.wav'))
bassB2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/B2.wav'))
bassC2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/C2.wav'))
bassD2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/D2.wav'))
bassE2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/E2.wav'))
bassF2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/F2.wav'))
bassG2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/G2.wav'))
bassCSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/C#2.wav'))
bassDSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/D#2.wav'))
bassFSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/F#2.wav'))
bassGSharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/G#2.wav'))
bassASharp2 = pygame.mixer.Sound(os.path.join(dir, './Sound Effects/Piano/A#2.wav'))

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
instruments = [True, False]
piano = True

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

#Set up the window
Surface    = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Music Maker')

#Variables
record = False

volumeSliderX = 50
volume = 1
activeSlider = False;
reverbSliderX = 25
reverb = 500
activeSlider2 = False;

infoWindow = False;
infoWindowX = windowWidth
iButtonPressed = False;
buttonPressed = False
buttonPressed2 = False
keyDown = False
keyDown2 = False

octaveWindow = False
octaveWindowX = windowWidth/3.55
octaveWindowHeight = 10
qButtonPressed = False

recordButton = False

#Mouse Variables
mousePosition = pygame.mouse.get_pos()
mousePressed  = pygame.mouse.get_pressed()

#Text Functions
def text_objects(Text, font, colour):
     textSurface = font.render(Text, True, colour)
     return textSurface, textSurface.get_rect()

def Text(Text, xPos, yPos, Size, Colour):
     largeText          = pygame.font.Font('Fonts/Times_New_Roman_Normal.ttf', Size)
     TextSurf, TextRect = text_objects(Text, largeText, Colour)
     TextRect.center    = (xPos, yPos)

     Surface.blit(TextSurf, TextRect)

rButtonPressed = False

while True: #Game Loop
    #Mouse Pressed info button
    if (Mouse.Pressed()[0] and Mouse.Position()[0] >= windowWidth-30 and Mouse.Position()[0] <= windowWidth-10 and Mouse.Position()[1] >= 9 and Mouse.Position()[1] <= 29):
        if (buttonPressed == False):
            if (infoWindow == True):
                infoWindow = False
            elif (infoWindow == False):
                infoWindow = True

            iButtonPressed = True
            buttonPressed = True
    elif (keyDown == False):
        iButtonPressed = False
        buttonPressed = False

    #pygame.draw.rect(Surface, SkyBlue, (windowWidth-906, 9, 20, 20))
    
    if (Mouse.Pressed()[0] and Mouse.Position()[0] >= windowWidth-906 and Mouse.Position()[0] <= windowWidth-906+20 and Mouse.Position()[1] >= 9 and Mouse.Position()[1] <= 29):
        if (buttonPressed2 == False):
            if (octaveWindow == True):
                octaveWindow = False
            elif (octaveWindow == False):
                octaveWindow = True

            qButtonPressed = True
            buttonPressed2 = True
    elif (keyDown2 == False):
        qButtonPressed = False
        buttonPressed2 = False
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:        
            #Open info window
            if (event.key == K_i):
                iButtonPressed = True
                keyDown = True

            #Open octive window
            if (event.key == K_q):
                qButtonPressed = True
<<<<<<< HEAD
=======
                keyDown = True

            #Instrument change
##            if (event.key == K_m):
##                qButtonPressed = True
##                keyDown = True
                
>>>>>>> 855292da16da3138e2d8e4f5dc062f4406c26229
                keyDown2 = True
            
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
            #I button
            if (event.key == K_i):
                if (infoWindow == True):
                    infoWindow = False
                elif (infoWindow == False):
                    infoWindow = True
                
                iButtonPressed = False
                keyDown = False

            #Octive Button
            if (event.key == K_q):
                if (octaveWindow == True):
                    octaveWindow = False
                elif (octaveWindow == False):
                    octaveWindow = True

                qButtonPressed = False
                keyDown2 = False

            #Record Button
            if (event.key == K_r):
                if (record == True):
                    record = False
                elif (record == False):
                    record = True
            
            #Notes Released
            if (event.key == K_a):
                noteColorsWhite[0] = (255, 255, 255)
                pianoTilesA[len(pianoTilesA)-1][3] = False
                
                C2.fadeout(reverb)
                C3.fadeout(reverb)
            if (event.key == K_s):
                noteColorsWhite[1] = (255, 255, 255)
                pianoTilesS[len(pianoTilesS)-1][3] = False
                
                D2.fadeout(reverb)
                D3.fadeout(reverb)
            if (event.key == K_d):
                noteColorsWhite[2] = (255, 255, 255)
                pianoTilesD[len(pianoTilesD)-1][3] = False
                
                E2.fadeout(reverb)
                E3.fadeout(reverb)
            if (event.key == K_f):
                noteColorsWhite[3] = (255, 255, 255)
                pianoTilesF[len(pianoTilesF)-1][3] = False
                
                F2.fadeout(reverb)
                F3.fadeout(reverb)
            if (event.key == K_g):
                noteColorsWhite[4] = (255, 255, 255)
                pianoTilesG[len(pianoTilesG)-1][3] = False
                
                G2.fadeout(reverb)
                G3.fadeout(reverb)
            if (event.key == K_h):
                noteColorsWhite[5] = (255, 255, 255)
                pianoTilesH[len(pianoTilesH)-1][3] = False

                A2.fadeout(reverb)
                A3.fadeout(reverb)
            if (event.key == K_j):
                noteColorsWhite[6] = (255, 255, 255)
                pianoTilesJ[len(pianoTilesJ)-1][3] = False
                
                B2.fadeout(reverb)
                B3.fadeout(reverb)
            if (event.key == K_k):
                noteColorsWhite[7] = (255, 255, 255)
                pianoTilesK[len(pianoTilesK)-1][3] = False
                
                C3.fadeout(reverb)
                C4.fadeout(reverb)
            if (event.key == K_l):
                noteColorsWhite[8] = (255, 255, 255)
                pianoTilesL[len(pianoTilesL)-1][3] = False

                D3.fadeout(reverb)
                D4.fadeout(reverb)
            if (event.key == K_SEMICOLON):
                noteColorsWhite[9] = (255, 255, 255)
                pianoTilesSEMI[len(pianoTilesSEMI)-1][3] = False
                
                E3.fadeout(reverb)
                E4.fadeout(reverb)
            if (event.key == K_w):
                noteColorsBlack[0] = (0, 0, 0)
                blackNoteKeys[6]   = (255, 255, 255)
                pianoTilesW[len(pianoTilesW)-1][3] = False
                
                CSharp2.fadeout(reverb)
                CSharp3.fadeout(reverb)
            if (event.key == K_e):
                noteColorsBlack[1] = (0, 0, 0)
                blackNoteKeys[5]   = (255, 255, 255)
                pianoTilesE[len(pianoTilesE)-1][3] = False
                
                DSharp2.fadeout(reverb)
                DSharp3.fadeout(reverb)
            if (event.key == K_t):
                noteColorsBlack[2] = (0, 0, 0)
                blackNoteKeys[4]   = (255, 255, 255)
                pianoTilesT[len(pianoTilesT)-1][3] = False
                
                FSharp2.fadeout(reverb)
                FSharp3.fadeout(reverb)
            if (event.key == K_y):
                noteColorsBlack[3] = (0, 0, 0)
                blackNoteKeys[3]   = (255, 255, 255)
                pianoTilesY[len(pianoTilesY)-1][3] = False

                GSharp2.fadeout(reverb)
                GSharp3.fadeout(reverb)
            if (event.key == K_u):
                noteColorsBlack[4] = (0, 0, 0)
                blackNoteKeys[2]   = (255, 255, 255)
                pianoTilesU[len(pianoTilesU)-1][3] = False

                ASharp2.fadeout(reverb)
                ASharp3.fadeout(reverb)
            if (event.key == K_o):
                noteColorsBlack[5] = (0, 0, 0)
                blackNoteKeys[1]   = (255, 255, 255)
                pianoTilesO[len(pianoTilesO)-1][3] = False

                CSharp3.fadeout(reverb)
                CSharp4.fadeout(reverb)
            if (event.key == K_p):
                noteColorsBlack[6] = (0, 0, 0)
                blackNoteKeys[0]   = (255, 255, 255)
                pianoTilesP[len(pianoTilesP)-1][3] = False
                
                DSharp3.fadeout(reverb)
                DSharp4.fadeout(reverb)
    
    #Change Volume
    volume = volumeSliderX/50

    Function.ChangeVolume(A2, volume)
    Function.ChangeVolume(B2, volume)
    Function.ChangeVolume(C2, volume)
    Function.ChangeVolume(D2, volume)
    Function.ChangeVolume(E2, volume)
    Function.ChangeVolume(F2, volume)
    Function.ChangeVolume(G2, volume)
    Function.ChangeVolume(CSharp2, volume)
    Function.ChangeVolume(DSharp2, volume)
    Function.ChangeVolume(FSharp2, volume)
    Function.ChangeVolume(GSharp2, volume)
    Function.ChangeVolume(ASharp2, volume)
    Function.ChangeVolume(A3, volume)
    Function.ChangeVolume(B3, volume)
    Function.ChangeVolume(C3, volume)
    Function.ChangeVolume(D3, volume)
    Function.ChangeVolume(E3, volume)
    Function.ChangeVolume(F3, volume)
    Function.ChangeVolume(G3, volume)
    Function.ChangeVolume(CSharp3, volume)
    Function.ChangeVolume(DSharp3, volume)
    Function.ChangeVolume(FSharp3, volume)
    Function.ChangeVolume(GSharp3, volume)
    Function.ChangeVolume(ASharp3, volume)
    Function.ChangeVolume(C4, volume)
    Function.ChangeVolume(D4, volume)
    Function.ChangeVolume(E4, volume)
    Function.ChangeVolume(CSharp4, volume)
    Function.ChangeVolume(DSharp4, volume)

    #Change Reverb
    reverb = reverbSliderX*20

    #Move Bars
    mousePressed = Mouse.Pressed()
    mousePosition = Mouse.Position()
    
    if (activeSlider2 == False and mousePressed[0] == 1 and mousePosition[0] <= (windowWidth-875)+135 and mousePosition[0] >= (windowWidth-875+35) and mousePosition[1] >= 16 and mousePosition[1] <= 21 or
        activeSlider2 == False and mousePressed[0] == 1 and mousePosition[0] <= (windowWidth-880)+volumeSliderX+45 and mousePosition[0] >= (windowWidth-880+35)+volumeSliderX and mousePosition[1] >= 11 and mousePosition[1] <= 26):
        activeSlider = True

    if (activeSlider):
        volumeSliderX = mousePosition[0]-440
        if (mousePressed[0] == 0):
            activeSlider = False

    if (volumeSliderX > 100):
        volumeSliderX = 100
    elif (volumeSliderX < 0):
        volumeSliderX = 0

    if (activeSlider == False and mousePressed[0] == 1 and mousePosition[0] <= (windowWidth-725)+reverbSliderX+45 and mousePosition[0] >= (windowWidth-725+35)+reverbSliderX and mousePosition[1] >= 11 and mousePosition[1] <= 26 or
        activeSlider == False and mousePressed[0] == 1 and mousePosition[0] <= (windowWidth-725)+135 and mousePosition[0] >= (windowWidth-725+35) and mousePosition[1] >= 16 and mousePosition[1] <= 21):
        activeSlider2 = True

    if (activeSlider2):
        reverbSliderX = mousePosition[0]-(555+35)
        if (mousePressed[0] == 0):
            activeSlider2 = False

    if (reverbSliderX > 100):
        reverbSliderX = 100
    elif (reverbSliderX < 0):
        reverbSliderX = 0

    #Background
    Draw.Background()

    #Instrument tab
    pygame.draw.rect(Surface, Black, (0, 0, windowWidth/3.55, windowHeight/1.75), 3)
    Text("Instruments", windowWidth-100, 18, 15, Black)

    #Delete Tiles
    Draw.DeleteTiles(pianoTilesA)
    Draw.DeleteTiles(pianoTilesS)
    Draw.DeleteTiles(pianoTilesD)
    Draw.DeleteTiles(pianoTilesF)
    Draw.DeleteTiles(pianoTilesG)
    Draw.DeleteTiles(pianoTilesH)
    Draw.DeleteTiles(pianoTilesJ)
    Draw.DeleteTiles(pianoTilesK)
    Draw.DeleteTiles(pianoTilesL)
    Draw.DeleteTiles(pianoTilesSEMI)
    Draw.DeleteTiles(pianoTilesW)
    Draw.DeleteTiles(pianoTilesE)
    Draw.DeleteTiles(pianoTilesT)
    Draw.DeleteTiles(pianoTilesY)
    Draw.DeleteTiles(pianoTilesU)
    Draw.DeleteTiles(pianoTilesO)
    Draw.DeleteTiles(pianoTilesP)

    #Move Tiles
    Draw.MoveTiles(pianoTilesA)
    Draw.MoveTiles(pianoTilesS)
    Draw.MoveTiles(pianoTilesD)
    Draw.MoveTiles(pianoTilesF)
    Draw.MoveTiles(pianoTilesG)
    Draw.MoveTiles(pianoTilesH)
    Draw.MoveTiles(pianoTilesJ)
    Draw.MoveTiles(pianoTilesK)
    Draw.MoveTiles(pianoTilesL)
    Draw.MoveTiles(pianoTilesSEMI)
    Draw.MoveTiles(pianoTilesW)
    Draw.MoveTiles(pianoTilesE)
    Draw.MoveTiles(pianoTilesT)
    Draw.MoveTiles(pianoTilesY)
    Draw.MoveTiles(pianoTilesU)
    Draw.MoveTiles(pianoTilesO)
    Draw.MoveTiles(pianoTilesP)

    #Draw Tiles
    Draw.DrawTiles(pianoTilesA)
    Draw.DrawTiles(pianoTilesS)
    Draw.DrawTiles(pianoTilesD)
    Draw.DrawTiles(pianoTilesF)
    Draw.DrawTiles(pianoTilesG)
    Draw.DrawTiles(pianoTilesH)
    Draw.DrawTiles(pianoTilesJ)
    Draw.DrawTiles(pianoTilesK)
    Draw.DrawTiles(pianoTilesL)
    Draw.DrawTiles(pianoTilesSEMI)
    Draw.DrawBlackTiles(pianoTilesW)
    Draw.DrawBlackTiles(pianoTilesE)
    Draw.DrawBlackTiles(pianoTilesT)
    Draw.DrawBlackTiles(pianoTilesY)
    Draw.DrawBlackTiles(pianoTilesU)
    Draw.DrawBlackTiles(pianoTilesO)
    Draw.DrawBlackTiles(pianoTilesP)

    #Octave Button
    if (octaveWindow):
        octaveWindowHeight += 50
        if (octaveWindowHeight >= 300):
            octaveWindowHeight = 300
    else:
        octaveWindowHeight -= 50
        if (octaveWindowHeight <= 10):
            octaveWindowHeight = 10

    pygame.draw.rect(Surface, LightGrey, (windowWidth/3.4, 10, windowWidth/3.2, octaveWindowHeight))
    pygame.draw.rect(Surface, Black, (windowWidth/3.4, 10, windowWidth/3.2, octaveWindowHeight), 2)
    
    #Top Bar
    Draw.TopBar()

    #Record Button
    if (record):
        pygame.draw.rect(Surface, Grey2, (windowWidth-459, 8, 20, 20))
        pygame.draw.rect(Surface, Green, (windowWidth-459, 8, 20, 20), 1)
        Text("•", windowWidth-449, 18, 35, Green)
    else:
        pygame.draw.rect(Surface, Grey2, (windowWidth-459, 8, 20, 20))
        pygame.draw.rect(Surface, Red, (windowWidth-459, 8, 20, 20), 1)
        Text("•", windowWidth-449, 18, 35, Red)
    
    #Draw Piano
    Draw.WhiteKey(windowWidth-92 , windowHeight-247, noteColorsWhite[9])
    Draw.WhiteKey(windowWidth-184, windowHeight-247, noteColorsWhite[8])
    Draw.WhiteKey(windowWidth-276, windowHeight-247, noteColorsWhite[7])
    Draw.WhiteKey(windowWidth-368, windowHeight-247, noteColorsWhite[6])
    Draw.WhiteKey(windowWidth-460, windowHeight-247, noteColorsWhite[5])
    Draw.WhiteKey(windowWidth-552, windowHeight-247, noteColorsWhite[4])
    Draw.WhiteKey(windowWidth-644, windowHeight-247, noteColorsWhite[3])
    Draw.WhiteKey(windowWidth-736, windowHeight-247, noteColorsWhite[2])
    Draw.WhiteKey(windowWidth-828, windowHeight-247, noteColorsWhite[1])
    Draw.WhiteKey(windowWidth-920, windowHeight-247, noteColorsWhite[0])
    
    Draw.BlackKey(windowWidth-116, windowHeight-247, noteColorsBlack[6])
    Draw.BlackKey(windowWidth-208, windowHeight-247, noteColorsBlack[5])
    Draw.BlackKey(windowWidth-392, windowHeight-247, noteColorsBlack[4])
    Draw.BlackKey(windowWidth-484, windowHeight-247, noteColorsBlack[3])
    Draw.BlackKey(windowWidth-577, windowHeight-247, noteColorsBlack[2])
    Draw.BlackKey(windowWidth-761, windowHeight-247, noteColorsBlack[1])
    Draw.BlackKey(windowWidth-853, windowHeight-247, noteColorsBlack[0])

    #Key Text
    Draw.WhiteKeyText(noteButtonList)
    Draw.BlackKeyText(blackNoteKeys)

    #Volume Slider
    Draw.VolumeSlider(volumeSliderX, activeSlider)

    #Reverb Slider
    Draw.ReverbSlider(reverbSliderX, activeSlider2)
    
    #Info Icon
    if (iButtonPressed):
        pygame.draw.rect(Surface, DarkSkyBlue, (windowWidth-30, 9, 20, 20))
    else:
        pygame.draw.rect(Surface, SkyBlue, (windowWidth-30, 9, 20, 20))
    pygame.draw.rect(Surface, Black, (windowWidth-30, 9, 20, 20), 1)
    Text("i", windowWidth-20, 19, 18, Black)

    #Octive Icon
    if (qButtonPressed):
        pygame.draw.rect(Surface, DarkSkyBlue, (windowWidth-906, 9, 20, 20))
    else:
        pygame.draw.rect(Surface, SkyBlue, (windowWidth-906, 9, 20, 20))
    pygame.draw.rect(Surface, Black, (windowWidth-906, 9, 20, 20), 1)
    Text("Q", windowWidth-895, 18, 15, Black)
    
    #Draw Info Window
    if (infoWindow):
        infoWindowX -= 75
        if (infoWindowX <= windowWidth-490):
            infoWindowX = windowWidth-490
    else:
        infoWindowX += 75
        if (infoWindowX >= windowWidth):
            infoWindowX = windowWidth

    pygame.draw.rect(Surface, LightGrey, (infoWindowX, 50, 500, 200))
    pygame.draw.rect(Surface, Black, (infoWindowX, 50, 500, 200), 2)
    
    pygame.display.flip()
    fpsClock.tick(FPS)
