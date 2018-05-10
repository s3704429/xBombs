'''
Created on 10 Apr. 2018

@author: bob
'''
import pygame
from bomb import *


def playerKeys(keypress, myboard, players, bombs):
    # for player 1 movement
    if keypress[pygame.K_UP]:
        players[0].moveUp(myboard)        
            
    if keypress[pygame.K_DOWN]:
        players[0].moveDown(myboard)
            
    if keypress[pygame.K_LEFT]:
        players[0].moveLeft(myboard)
         
    if keypress[pygame.K_RIGHT]:
        players[0].moveRight(myboard)
    
    if keypress[pygame.K_KP0]:
        players[0].dropBomb(myboard, bombs)
            
    if keypress[pygame.K_UP] != True and keypress[pygame.K_RIGHT] != True and keypress[pygame.K_LEFT] != True and keypress[pygame.K_DOWN] != True:
        players[0].standing = True
    
    # for player 2 movement
    if keypress[pygame.K_w]:
        players[1].moveUp(myboard)
            
    if keypress[pygame.K_s]:
        players[1].moveDown(myboard)            
            
    if keypress[pygame.K_a]:
        players[1].moveLeft(myboard)
         
            
    if keypress[pygame.K_d]:
        players[1].moveRight(myboard)
                
                
    if keypress[pygame.K_q]:
        players[1].dropBomb(myboard, bombs)

    if keypress[pygame.K_w] != True and keypress[pygame.K_a] != True and keypress[pygame.K_s] != True and keypress[pygame.K_d] != True:
        players[1].standing = True
    
    if len(players) > 2:    
        # for player 3 movement
        if keypress[pygame.K_KP8]:
            players[2].moveUp(myboard)
                
        if keypress[pygame.K_KP5]:
            players[2].moveDown(myboard)            
                
        if keypress[pygame.K_KP4]:
            players[2].moveLeft(myboard)
             
                
        if keypress[pygame.K_KP6]:
            players[2].moveRight(myboard)
                    
                    
        if keypress[pygame.K_KP7]:
            players[2].dropBomb(myboard, bombs)
    
        if keypress[pygame.K_KP8] != True and keypress[pygame.K_KP5] != True and keypress[pygame.K_KP4] != True and keypress[pygame.K_KP6] != True:
            players[2].standing = True
            
    if len(players) > 3:      
        # for player 4 movement
        if keypress[pygame.K_u]:
            players[3].moveUp(myboard)
                
        if keypress[pygame.K_j]:
            players[3].moveDown(myboard)            
                
        if keypress[pygame.K_h]:
            players[3].moveLeft(myboard)
             
                
        if keypress[pygame.K_k]:
            players[3].moveRight(myboard)
                    
                    
        if keypress[pygame.K_y]:
            players[3].dropBomb(myboard, bombs)
    
        if keypress[pygame.K_u] != True and keypress[pygame.K_j] != True and keypress[pygame.K_h] != True and keypress[pygame.K_k] != True:
            players[3].standing = True
            
    