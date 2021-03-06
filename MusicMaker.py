#https://stackoverflow.com/questions/9770073/sound-generation-synthesis-with-python
#https://soledadpenades.com/posts/2009/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/

from MusicMakerClasses import *

FPS=30
fpsClock=pygame.time.Clock()

recordList = []
recordButton = []
recordNoteStart = []
recordNoteLength = []

recordingNotes = []
recordingTime = []
notes = []
recordingNames = []
highestRecording = 0

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
currentOctive   = [False, True, False]
instruments = [True, False]

#Set up the window
Surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Music Maker')

#Variables
recordingY = 48

record = False
recordWindow = False

volumeSliderX = 50
volume = 1
activeSlider = False
reverbSliderX = 25
reverb = 500
activeSlider2 = False

infoWindow = False
infoWindowX = windowWidth
iButtonPressed = False
buttonPressed = False
buttonPressed2 = False
buttonPressed3 = False
keyDown = False
keyDown2 = False

octaveWindow = False
octaveWindowX = windowWidth/3.55
octaveWindowHeight = 10
qButtonPressed = False

noPressed = False
yesPressed = False

octave = 0
currentKeys = 0

#Mouse Variables
mousePosition = pygame.mouse.get_pos()
mousePressed  = pygame.mouse.get_pressed()

#Functions
def findRecordings():
    recordingNames.clear()
    recordingNotes.clear()
    notes = []
    
    for i in os.listdir("./Recordings"):
        if (i[0] != "."):
            recordingNames.append(i)     

    for recording in recordingNames:
        file = open("./Recordings/" + str(recording), "r")

        numNotes = 0
        noteLines = 0
        line = file.readline()
        line = file.readline()
        while (line != ""):
            noteLines += 1
            line = file.readline()
            if (noteLines == 5):
                numNotes += 1
                noteLines = 0
        file.close()

        file = open("./Recordings/" + str(recording), "r")
        recordingTime = file.readline()
        for i in range(numNotes):
            noteStartTime = file.readline()
            noteLength = file.readline()
            typeOfNote = file.readline()
            noteKeyPressed = file.readline()
            noteOctive = file.readline()

            notes.append((noteStartTime.rstrip(), noteLength.rstrip(), typeOfNote.rstrip(), noteKeyPressed.rstrip(), noteOctive.rstrip()))

            if (i == numNotes-1):
                for note in notes:
                    tempRecordNotes = []
                    tempRecordNotes.append((note[0], note[1], note[2], note[3], note[4]))

                recordingNotes.append(tempRecordNotes)
                tempRecordNotes = []

while True: #Loop
    #Mouse Pressed info button
    if (record == False and recordWindow == False and Mouse.Pressed()[0] and Mouse.Position()[0] >= windowWidth-30 and Mouse.Position()[0] <= windowWidth-10 and Mouse.Position()[1] >= 9 and Mouse.Position()[1] <= 29):
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

    #Mouse Pressed octive button
    if (record == False and recordWindow == False and Mouse.Pressed()[0] and Mouse.Position()[0] >= windowWidth-906 and Mouse.Position()[0] <= windowWidth-906+20 and Mouse.Position()[1] >= 9 and Mouse.Position()[1] <= 29):
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

    #Mouse Pressed the instruments
    if (instruments[0] == False and Mouse.Pressed()[0] and Mouse.Position()[0] >= 10 and Mouse.Position()[0] < 100 and Mouse.Position()[1] >= 520 and Mouse.Position()[1] <= 570):
        instruments[0] = True
        instruments[1] = False

    if (instruments[1] == False and Mouse.Pressed()[0] and Mouse.Position()[0] >= 10 and Mouse.Position()[0] < 100 and Mouse.Position()[1] >= 570 and Mouse.Position()[1] <= 620):
        instruments[0] = False
        instruments[1] = True
  
    if (record == False and recordWindow == False and Mouse.Pressed()[0] and Mouse.Position()[0] >= windowWidth-459-14 and Mouse.Position()[0] <= windowWidth-459-14+20 and Mouse.Position()[1] >= 9 and Mouse.Position()[1] <= 29):
        if (buttonPressed3 == False):
            if (record == True):
                if (len(recordList) > 0):
                    recordWindow = True
                length = round(time.time() - recordBeginTime, 3)
                record = False
                print(length, recordList)
                recordBeginTime = 0
                recordLength = 0
                recordList = []
            elif (record == False):
                record = True
                recordBeginTime = time.time()

            buttonPressed3 = True
    else:
        buttonPressed3 = False
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and recordWindow == False:
            #Record
            if (record and event.key != K_r):
                recordNoteStart.append(round(time.time() - recordBeginTime, 3))
            
            #Open info window
            if (event.key == K_i):
                iButtonPressed = True
                keyDown = True

            #Open octive window
            if (event.key == K_q):
                qButtonPressed = True
                keyDown2 = True

            #Moves Octive down
            if (event.key == K_z):
                if (currentOctive[1] == True):
                    currentOctive[1] = False
                    currentOctive[0] = True
                    octave = -1
                if (currentOctive[2] == True):
                    currentOctive[2] = False
                    currentOctive[1] = True
                    octave = 0

            #Moves Octive up
            if (event.key == K_x):
                if (currentOctive[1] == True):
                    currentOctive[1] = False
                    currentOctive[2] = True
                    octave = 1
                if (currentOctive[0] == True):
                    currentOctive[0] = False
                    currentOctive[1] = True
                    octave = 0

            #Resets octive to base
            if (event.key == K_c):
                currentOctive[1] = True
                currentOctive[0] = False
                currentOctive[2] = False
                octave = 0

            #Piano button
            if (event.key == K_1):
                instruments = [True, False]

            #Bass button
            if (event.key == K_2):
                instruments = [False, True]

            if (event.key == K_a):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("C", "a", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("C", "a", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("C", "a", "lowOctive"))
                noteColorsWhite[0] = (0, 255, 0)
                pianoTilesA.append([windowWidth-920, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        C1.play()
                    elif (currentOctive[1] == True):
                        C2.play()
                    elif (currentOctive[2] == True):
                        C3.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_s):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("D", "s", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("D", "s", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("D", "s", "lowOctive"))
                noteColorsWhite[1] = (0, 255, 0)
                pianoTilesS.append([windowWidth-828, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        D1.play()
                    elif (currentOctive[1] == True):
                        D2.play()
                    elif (currentOctive[2] == True):
                        D3.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_d):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("E", "d", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("E", "d", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("E", "d", "lowOctive"))
                noteColorsWhite[2] = (0, 255, 0)
                pianoTilesD.append([windowWidth-736, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        E1.play()
                    elif (currentOctive[1] == True):
                        E2.play()
                    elif (currentOctive[2] == True):
                        E3.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_f):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("F", "f", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("F", "f", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("F", "f", "lowOctive"))
                noteColorsWhite[3] = (0, 255, 0)
                pianoTilesF.append([windowWidth-644, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        F1.play()
                    elif (currentOctive[1] == True):
                        F2.play()
                    elif (currentOctive[2] == True):
                        F3.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_g):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("G", "g", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("G", "g", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("G", "g", "lowOctive"))
                noteColorsWhite[4] = (0, 255, 0)
                pianoTilesG.append([windowWidth-552, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        G1.play()
                    elif (currentOctive[1] == True):
                        G2.play()
                    elif (currentOctive[2] == True):
                        G3.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_h):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("A", "h", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("A", "h", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("A", "h", "lowOctive"))
                noteColorsWhite[5] = (0, 255, 0)
                pianoTilesH.append([windowWidth-460, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        A1.play()
                    elif (currentOctive[1] == True):
                        A2.play()
                    elif (currentOctive[2] == True):
                        A3.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_j):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("B", "j", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("B", "j", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("B", "j", "lowOctive"))
                noteColorsWhite[6] = (0, 255, 0)
                pianoTilesJ.append([windowWidth-368, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        B1.play()
                    elif (currentOctive[1] == True):
                        B2.play()
                    elif (currentOctive[2] == True):
                        B3.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_k):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("C", "k", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("C", "k", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("C", "k", "lowOctive"))
                noteColorsWhite[7] = (0, 255, 0)
                pianoTilesK.append([windowWidth-276, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        C2.play()
                    elif (currentOctive[1] == True):
                        C3.play()
                    elif (currentOctive[2] == True):
                        C4.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_l):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("D", "l", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("D", "l", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("D", "l", "lowOctive"))
                noteColorsWhite[8] = (0, 255, 0)
                pianoTilesL.append([windowWidth-184, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        D2.play()
                    elif (currentOctive[1] == True):
                        D3.play()
                    elif (currentOctive[2] == True):
                        D4.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_SEMICOLON):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("E", "SEMI", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("E", "SEMI", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("E", "SEMI", "lowOctive"))
                noteColorsWhite[9] = (0, 255, 0)
                pianoTilesSEMI.append([windowWidth-92, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        E2.play()
                    elif (currentOctive[1] == True):
                        E3.play()
                    elif (currentOctive[2] == True):
                        E4.play()
                if (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_w):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("CSharp", "w", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("CSharp", "w", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("CSharp", "w", "lowOctive"))
                noteColorsBlack[0] = (0  , 150, 0  )
                blackNoteKeys[6]   = (0, 0, 0)
                pianoTilesW.append([windowWidth-853, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        CSharp1.play()
                    elif (currentOctive[1] == True):
                        CSharp2.play()
                    elif (currentOctive[2] == True):
                        CSharp3.play()
                elif (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_e):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("DSharp", "e", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("DSharp", "e", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("DSharp", "e", "lowOctive"))
                noteColorsBlack[1] = (0  , 150, 0  )
                blackNoteKeys[5]   = (0, 0, 0)
                pianoTilesE.append([windowWidth-761, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        DSharp1.play()
                    elif (currentOctive[1] == True):
                        DSharp2.play()
                    elif (currentOctive[2] == True):
                        DSharp3.play()
                elif (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_t):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("FSharp", "t", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("FSharp", "t", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("FSharp", "t", "lowOctive"))
                noteColorsBlack[2] = (0  , 150, 0  )
                blackNoteKeys[4]   = (0, 0, 0)
                pianoTilesT.append([windowWidth-577, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        FSharp1.play()
                    elif (currentOctive[1] == True):
                        FSharp2.play()
                    elif (currentOctive[2] == True):
                        FSharp3.play()
                elif (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_y):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("GSharp", "y", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("GSharp", "y", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("GSharp", "y", "lowOctive"))
                noteColorsBlack[3] = (0  , 150, 0  )
                blackNoteKeys[3]   = (0, 0, 0)
                pianoTilesY.append([windowWidth-484, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        GSharp1.play()
                    elif (currentOctive[1] == True):
                        GSharp2.play()
                    elif (currentOctive[2] == True):
                        GSharp3.play()
                elif (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_u):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("ASharp", "u", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("ASharp", "u", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("ASharp", "u", "lowOctive"))
                noteColorsBlack[4] = (0  , 150, 0  )
                blackNoteKeys[2]   = (0, 0, 0)
                pianoTilesU.append([windowWidth-392, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        ASharp1.play()
                    elif (currentOctive[1] == True):
                        ASharp2.play()
                    elif (currentOctive[2] == True):
                        ASharp3.play()
                elif (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_o):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("CSharp", "o", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("CSharp", "o", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("CSharp", "o", "lowOctive"))
                noteColorsBlack[5] = (0  , 150, 0  )
                blackNoteKeys[1]   = (0, 0, 0)
                pianoTilesO.append([windowWidth-208, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        CSharp2.play()
                    elif (currentOctive[1] == True):
                        CSharp3.play()
                    elif (currentOctive[2] == True):
                        CSharp4.play()
                elif (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            if (event.key == K_p):
                if (record):
                    if (currentOctive[1]):
                        recordButton.append(("DSharp", "p", "midOctive"))
                    elif (currentOctive[2]):
                        recordButton.append(("DSharp", "p", "highOctive"))
                    elif (currentOctive[0]):
                        recordButton.append(("DSharp", "p", "lowOctive"))
                noteColorsBlack[6] = (0  , 150, 0  )
                blackNoteKeys[0]   = (0, 0, 0)
                pianoTilesP.append([windowWidth-116, windowHeight-247, 0, True])
                currentKeys += 1
                if (instruments[0]):
                    if (currentOctive[0] == True):
                        DSharp1.play()
                    elif (currentOctive[1] == True):
                        DSharp2.play()
                    elif (currentOctive[2] == True):
                        DSharp3.play()
                elif (instruments[1]):
                    if (currentOctive[0] == True):
                        print("bass note")
                    elif (currentOctive[1] == True):
                        print("bass note")
                    elif (currentOctive[2] == True):
                        print("bass note")
            
        if event.type == KEYUP and recordWindow == False:
            #Record Notes
            if (record and event.key != K_r):
                length = time.time() - recordBeginTime
                for i in range(len(recordButton)):
                    recordNoteLength.append(round(length - recordNoteStart[i], 3))
                    recordList.append((recordNoteStart[i], recordNoteLength[i], recordButton[i][0], recordButton[i][1], recordButton[i][2]))
                recordButton = None
                startLength = False
                recordNoteStart = []
                recordNoteLength = []
                recordButton = []


            #Info button
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
                if (record == True and keyboardIdle == True):
                    if (len(recordList) > 0):
                        recordWindow = True
                    record = False
                    endTime = round(time.time() - recordBeginTime, 3)
                    length = round(time.time() - recordBeginTime, 3)
                elif (record == False):
                    record = True
                    recordBeginTime = time.time()
            
            #Notes Released
            if (event.key == K_a):
                noteColorsWhite[0] = (255, 255, 255)
                pianoTilesA[len(pianoTilesA)-1][3] = False
                currentKeys -= 1

                C1.fadeout(reverb)
                C2.fadeout(reverb)
                C3.fadeout(reverb)
            if (event.key == K_s):
                noteColorsWhite[1] = (255, 255, 255)
                pianoTilesS[len(pianoTilesS)-1][3] = False
                currentKeys -= 1

                D1.fadeout(reverb)
                D2.fadeout(reverb)
                D3.fadeout(reverb)
            if (event.key == K_d):
                noteColorsWhite[2] = (255, 255, 255)
                pianoTilesD[len(pianoTilesD)-1][3] = False
                currentKeys -= 1

                E1.fadeout(reverb)
                E2.fadeout(reverb)
                E3.fadeout(reverb)
            if (event.key == K_f):
                noteColorsWhite[3] = (255, 255, 255)
                pianoTilesF[len(pianoTilesF)-1][3] = False
                currentKeys -= 1

                F1.fadeout(reverb)
                F2.fadeout(reverb)
                F3.fadeout(reverb)
            if (event.key == K_g):
                noteColorsWhite[4] = (255, 255, 255)
                pianoTilesG[len(pianoTilesG)-1][3] = False
                currentKeys -= 1

                G1.fadeout(reverb)
                G2.fadeout(reverb)
                G3.fadeout(reverb)
            if (event.key == K_h):
                noteColorsWhite[5] = (255, 255, 255)
                pianoTilesH[len(pianoTilesH)-1][3] = False
                currentKeys -= 1

                A1.fadeout(reverb)
                A2.fadeout(reverb)
                A3.fadeout(reverb)
            if (event.key == K_j):
                noteColorsWhite[6] = (255, 255, 255)
                pianoTilesJ[len(pianoTilesJ)-1][3] = False
                currentKeys -= 1

                B1.fadeout(reverb)
                B2.fadeout(reverb)
                B3.fadeout(reverb)
            if (event.key == K_k):
                noteColorsWhite[7] = (255, 255, 255)
                pianoTilesK[len(pianoTilesK)-1][3] = False
                currentKeys -= 1

                C2.fadeout(reverb)
                C3.fadeout(reverb)
                C4.fadeout(reverb)
            if (event.key == K_l):
                noteColorsWhite[8] = (255, 255, 255)
                pianoTilesL[len(pianoTilesL)-1][3] = False
                currentKeys -= 1

                D2.fadeout(reverb)
                D3.fadeout(reverb)
                D4.fadeout(reverb)
            if (event.key == K_SEMICOLON):
                noteColorsWhite[9] = (255, 255, 255)
                pianoTilesSEMI[len(pianoTilesSEMI)-1][3] = False
                currentKeys -= 1

                E2.fadeout(reverb)
                E3.fadeout(reverb)
                E4.fadeout(reverb)
            if (event.key == K_w):
                noteColorsBlack[0] = (0, 0, 0)
                blackNoteKeys[6]   = (255, 255, 255)
                pianoTilesW[len(pianoTilesW)-1][3] = False
                currentKeys -= 1

                CSharp1.fadeout(reverb)
                CSharp2.fadeout(reverb)
                CSharp3.fadeout(reverb)
            if (event.key == K_e):
                noteColorsBlack[1] = (0, 0, 0)
                blackNoteKeys[5]   = (255, 255, 255)
                pianoTilesE[len(pianoTilesE)-1][3] = False
                currentKeys -= 1

                DSharp1.fadeout(reverb)
                DSharp2.fadeout(reverb)
                DSharp3.fadeout(reverb)
            if (event.key == K_t):
                noteColorsBlack[2] = (0, 0, 0)
                blackNoteKeys[4]   = (255, 255, 255)
                pianoTilesT[len(pianoTilesT)-1][3] = False
                currentKeys -= 1

                FSharp1.fadeout(reverb)
                FSharp2.fadeout(reverb)
                FSharp3.fadeout(reverb)
            if (event.key == K_y):
                noteColorsBlack[3] = (0, 0, 0)
                blackNoteKeys[3]   = (255, 255, 255)
                pianoTilesY[len(pianoTilesY)-1][3] = False
                currentKeys -= 1

                GSharp1.fadeout(reverb)
                GSharp2.fadeout(reverb)
                GSharp3.fadeout(reverb)
            if (event.key == K_u):
                noteColorsBlack[4] = (0, 0, 0)
                blackNoteKeys[2]   = (255, 255, 255)
                pianoTilesU[len(pianoTilesU)-1][3] = False
                currentKeys -= 1

                ASharp1.fadeout(reverb)
                ASharp2.fadeout(reverb)
                ASharp3.fadeout(reverb)
            if (event.key == K_o):
                noteColorsBlack[5] = (0, 0, 0)
                blackNoteKeys[1]   = (255, 255, 255)
                pianoTilesO[len(pianoTilesO)-1][3] = False
                currentKeys -= 1

                CSharp2.fadeout(reverb)
                CSharp3.fadeout(reverb)
                CSharp4.fadeout(reverb)
            if (event.key == K_p):
                noteColorsBlack[6] = (0, 0, 0)
                blackNoteKeys[0]   = (255, 255, 255)
                pianoTilesP[len(pianoTilesP)-1][3] = False
                currentKeys -= 1

                DSharp2.fadeout(reverb)
                DSharp3.fadeout(reverb)
                DSharp4.fadeout(reverb)

    #Find Recordings
    findRecordings()
    
    #check if keyboard is currently in use
    if(currentKeys < 1):
        keyboardIdle = True
    else:
        keyboardIdle = False
        
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
    if (recordWindow == False):
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

    #Draw Recording Boxes
    for recording in recordingNames:
        Draw.recordingBox(recordingY)
        recordingY += 105
    recordingY = 48

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

    #octave window text
    Draw.OctaveWindowText(octaveWindowHeight, octave)
    
    #Top Bar
    Draw.TopBar()

    #Record Button
    Draw.RecordButton(record)
    
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
    Draw.Icon(iButtonPressed, qButtonPressed)
    
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

    #info Window Text
    Draw.InfoWindowText(infoWindowX)

    if (recordWindow):
        pygame.draw.rect(Surface, LightGrey, (windowWidth/2+25, windowHeight/2-200, 300, 200))
        pygame.draw.rect(Surface, Black, (windowWidth/2+25, windowHeight/2-200, 300, 200), 2)

        Text("Would you like to save", windowWidth/2+175, windowHeight/2-150, 25, Black)
        Text("this recording?"       , windowWidth/2+175, windowHeight/2-125, 25, Black)

        if (Mouse.Pressed()[0] and Mouse.Position()[0] >= windowWidth/2+50 and Mouse.Position()[0] <= windowWidth/2+160 and Mouse.Position()[1] >= windowHeight/2-70 and Mouse.Position()[1] <= windowHeight/2-20):
            pygame.draw.rect(Surface, Grey3, (windowWidth/2+50, windowHeight/2-70, 110, 50))
            pygame.draw.rect(Surface, Black, (windowWidth/2+50, windowHeight/2-70, 110, 50), 2)
            yesPressed = True
        elif (Mouse.Pressed()[0] == False and Mouse.Position()[0] >= windowWidth/2+50 and Mouse.Position()[0] <= windowWidth/2+160 and Mouse.Position()[1] >= windowHeight/2-70 and Mouse.Position()[1] <= windowHeight/2-20):
            pygame.draw.rect(Surface, LightGrey3, (windowWidth/2+50, windowHeight/2-70, 110, 50))
            pygame.draw.rect(Surface, Black, (windowWidth/2+50, windowHeight/2-70, 110, 50), 2)
        else:
            pygame.draw.rect(Surface, LightGrey2, (windowWidth/2+50, windowHeight/2-70, 110, 50))
            pygame.draw.rect(Surface, Black, (windowWidth/2+50, windowHeight/2-70, 110, 50), 2)
            yesPressed = False

        if (Mouse.Pressed()[0] and Mouse.Position()[0] >= windowWidth/2+190 and Mouse.Position()[0] <= windowWidth/2+300 and Mouse.Position()[1] >= windowHeight/2-70 and Mouse.Position()[1] <= windowHeight/2-20):
            pygame.draw.rect(Surface, Grey3, (windowWidth/2+190, windowHeight/2-70, 110, 50))
            pygame.draw.rect(Surface, Black, (windowWidth/2+190, windowHeight/2-70, 110, 50), 2)
            noPressed = True
        elif (Mouse.Pressed()[0] == False and Mouse.Position()[0] >= windowWidth/2+190 and Mouse.Position()[0] <= windowWidth/2+300 and Mouse.Position()[1] >= windowHeight/2-70 and Mouse.Position()[1] <= windowHeight/2-20):
            pygame.draw.rect(Surface, LightGrey3, (windowWidth/2+190, windowHeight/2-70, 110, 50))
            pygame.draw.rect(Surface, Black, (windowWidth/2+190, windowHeight/2-70, 110, 50), 2)
        else:
            pygame.draw.rect(Surface, LightGrey2, (windowWidth/2+190, windowHeight/2-70, 110, 50))
            pygame.draw.rect(Surface, Black, (windowWidth/2+190, windowHeight/2-70, 110, 50), 2)
            noPressed = False
        Text("Yes", windowWidth/2+105, windowHeight/2-45, 25, Black)
        Text("No" , windowWidth/2+245, windowHeight/2-45, 25, Black)

        if (noPressed):
            if (Mouse.Pressed()[0] == False):
                recordWindow = False
                noPressed = False

                recordBeginTime = 0
                recordLength = 0
                recordList = []
        if (yesPressed):
            if (Mouse.Pressed()[0] == False):
                recordWindow = False
                yesPressed = False

                highestRecording = 0
                for i in os.listdir("./Recordings"):
                    if (i[9].isdigit()):
                        highestRecording = int(i[9])

                #Append recording to save file
                recordingFile = open("Recordings/Recording" + str(highestRecording+1) + ".txt", "a")
                recordingFile.write(str(endTime) + "\n")
                for notes in recordList:
                    recordingFile.write(str(notes[0]) + "\n")
                    recordingFile.write(str(notes[1]) + "\n")
                    recordingFile.write(str(notes[2]) + "\n")
                    recordingFile.write(str(notes[3]) + "\n")
                    recordingFile.write(str(notes[4]) + "\n")
                recordingFile.close()

                recordBeginTime = 0
                recordLength = 0
                recordList = []

    Draw.PianoButton(instruments)
    Draw.BassButton(instruments)
    
    pygame.display.flip()
    fpsClock.tick(FPS)
