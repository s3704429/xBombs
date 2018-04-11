'''
Created on 10 Apr. 2018

@author: bob
'''
import pygame
from bomb import *

def playerKeys(keypress, myboard, player1, player2, bombs):
    # for player 1 movement
    if keypress[pygame.K_UP]:
        if player1.position[0] > 0 and myboard.getGridObject(player1.position, 0, -1) == 0:
            player1.position[0] -= 1
            
    if keypress[pygame.K_DOWN]:
        if player1.position[0] < 9 and myboard.getGridObject(player1.position, 0, 1) == 0:
            player1.position[0] += 1
            
            
    if keypress[pygame.K_LEFT]:
        if player1.position[1] > 0 and myboard.getGridObject(player1.position, -1, 0) == 0: 
            player1.position[1] -= 1
         
    if keypress[pygame.K_RIGHT]:
        if  player1.position[1] < 9 and myboard.getGridObject(player1.position, 1, 0) == 0:
            player1.position[1] += 1
    
    if keypress[pygame.K_KP0]:
        if player1.bombsTotal > 0:
            myboard.myboard[player1.position[0]][player1.position[1]] = Bomb('soft', 45, 1, player1, player1.position)
            bombs.append(player1.position);
            player1.bombsTotal -= 1
    
    
    # for player 2 movement
    if keypress[pygame.K_w]:
        if player2.position[0] > 0 and myboard.getGridObject(player2.position, 0, -1) == 0:
            player2.position[0] -= 1
            
    if keypress[pygame.K_s]:
        if player2.position[0] < 9 and myboard.getGridObject(player2.position, 0, 1) == 0:
            player2.position[0] += 1
            
            
    if keypress[pygame.K_a]:
        if player2.position[1] > 0  and myboard.getGridObject(player2.position, -1, 0) == 0:
            player2.position[1] -= 1
         
            
    if keypress[pygame.K_d]:
        if  player2.position[1] < 9 and myboard.getGridObject(player2.position, 1, 0) == 0:
            player2.position[1] += 1
                
                
    if keypress[pygame.K_q]:
        if player2.bombsTotal > 0:
            myboard.myboard[player2.position[0]][player2.position[1]] = Bomb('soft', 45, 1, player2, player2.position)
            bombs.append(player2.position);
            player2.bombsTotal -= 1
