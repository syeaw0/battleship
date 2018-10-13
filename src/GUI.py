###########
# IMPORTS #
###########
import pygame
import time

#############
# CONSTANTS #
#############

display_width = 800
display_height = 600
black = (0,0,0) #RGB concentrations
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

####################
# INITIALIZE BOARD #
####################

pygame.init() # initiates pygame
gameDisplay = pygame.display.set_mode ((display_width,display_height, )) #board size 
pygame.display.set_caption('Battleship') #game title

clock = pygame.time.Clock() #a real time clock

carrier = pygame.image.load('images/carrier.png').convert() #loads a carrier photo onto the carrier variable

def battleship(x,y):
    gameDisplay.blit(carrier,(x,y))


def text_objects(text,font):
    textSurface = font.render(text,True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',15)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()



def message_intro():
    message_display('Welcome to Battleship!')

    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        message_intro()

        mouse = pygame.mouse.get_pos()
        #print(mouse)

        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450: #if mouse coordinates are between (150,450), highlight the respected boxes
            pygame.draw.rect(gameDisplay, bright_green, (150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, green, (150,450,100,50))

        if 450+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450: 
            pygame.draw.rect(gameDisplay, bright_red, (450,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, red,(450,450,100,50))

 
        pygame.display.update()
        clock.tick(15)

        
def game_loop():
    x = (display_width * 0.1)
    y = (display_height * 0.1)


    gameExit = False #declares an end variable for when the user exits the game

    while not gameExit: #while the user doesn't exit out the game

###########################
# EVENT HANDLING LOOP     #
###########################
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if user presses the exit window
              pygame.quit()
              quit()
              
        gameDisplay.fill(white) # fills up entire GUI with white space
        battleship(x,y) #place battleship at x,y coordinates

        pygame.display.update() #will update the entire GUI
        clock.tick(60) #frames per second game. Can increase to 60

######
#MAIN#
######

game_intro()        
game_loop()


########
# EXIT #
########

pygame.quit() #quits pygame and closes the GUI
quit()
