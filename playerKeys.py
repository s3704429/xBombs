import pygame
from bomb import *


def playerKeys(keypress, myboard, player1, player2, bombs):
    # for player 1 movement
    if keypress[pygame.K_UP]:
        player1.moveUp(myboard)
                
            
    if keypress[pygame.K_DOWN]:
        player1.moveDown(myboard)
            
    if keypress[pygame.K_LEFT]:
        player1.moveLeft(myboard)
         
    if keypress[pygame.K_RIGHT]:
        player1.moveRight(myboard)
    
    if keypress[pygame.K_KP0]:
        if player1.bombsTotal > 0:
            player1.dropBomb(myboard, bombs)
            
    if keypress[pygame.K_UP] != True and keypress[pygame.K_RIGHT] != True and keypress[pygame.K_LEFT] != True and keypress[pygame.K_DOWN] != True:
        player1.standing = True
    
    # for player 2 movement
    if keypress[pygame.K_w]:
        player2.moveUp(myboard)
            
    if keypress[pygame.K_s]:
        player2.moveDown(myboard)            
            
    if keypress[pygame.K_a]:
        player2.moveLeft(myboard)
         
            
    if keypress[pygame.K_d]:
        player2.moveRight(myboard)
                
                
    if keypress[pygame.K_q]:
        if player2.bombsTotal > 0:
            player2.dropBomb(myboard, bombs)

    if keypress[pygame.K_w] != True and keypress[pygame.K_a] != True and keypress[pygame.K_s] != True and keypress[pygame.K_d] != True:
        player2.standing = True
    
