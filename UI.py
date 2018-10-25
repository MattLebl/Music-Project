import pygame, sys
from MusickMakerUI import Button
from MusickMakerUI import Record
pygame.init()

# Define some colours
WHITE = (255, 255, 255)
GRAY = (60 , 60 , 60 )
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

windowWidth = 1280
windowHeight = 720
window = (windowWidth, windowHeight)
screen = pygame.display.set_mode(window)
pygame.display.set_caption("Musik Maker")
level = 1

def my_next_function():
       print("it's working")
       
def mousebuttondown(level):
    """A function that checks which button was pressed"""
    pos = pygame.mouse.get_pos()
    if level == 1:
        for button in level1_buttons:
            if button.rect.collidepoint(pos):
                button.call_back()

level = 1
menuOn = True

#create buttons
button_record = Record("R", (windowWidth/2, windowHeight/3), my_next_function, bg=(50, 200, 20))
button_02 = Button("s", (windowWidth/2, windowHeight*2/3), my_next_function, bg=(50, 200, 20)) 

#arrange button groups depending on level
level1_buttons = [button_record, button_02]

clock = pygame.time.Clock()

while menuOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            menuOn = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown(level)

    # Get mouse location
    mouse = pygame.mouse.get_pos()
    #print (mouse) # Uncomment to see mouse position in shell

    # Check if mouse is pressed
    click = pygame.mouse.get_pressed()
    #print (click) # Uncomment to see mouse buttons clicked in shell
    
    # --- Draw code goes here

    # Clear the screen to white
    #Loads background and logo
    screen.fill(RED)
    #screen.blit(background, (0, 0))

    # Queue shapes to be drawn
    
    # Buttons
    #Loads the different menu levels with all of the buttons
    if level == 1:
        for button in level1_buttons:
            button.draw()

    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()

