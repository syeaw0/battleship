###########
# IMPORTS #
###########

import pygame


pygame.init() # initiates pygame
gameDisplay = pygame.display.set_mode ((800,600)) #board size 
pygame.display.set_caption('Battleship') #game title


clock = pygame.time.Clock() #a real time clock

crashed = False #declares an end variable for when the user exits the game

while not crashed: #while the user doesn't exit out the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if user presses the exit window
            crashed = True #sets crash to true and then ends the game

        print(event)

    pygame.display.update() #will update the entire GUI

    clock.tick(30) #frames per second game. Can increase to 60


pygame.quit() #quits pygame and closes the GUI
