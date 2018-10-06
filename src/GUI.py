###########
# IMPORTS #
###########

import pygame


pygame.init() # initiates pygame
gameDisplay = pygame.display.set_mode ((800,600))
pygame.display.set_caption('Battleship')


clock = pygame.time.Clock() #a real time clock

crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update() #will update the entire GUI

    clock.tick(30) #frames per second game. Can increase to 60


pygame.quit() #quits pygame
