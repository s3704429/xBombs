import pygame
from character import *
from terrain import *
from bomb import *
from mapGrid import *
from playerKeys import *

player1 = Character([9,9], "green")
player2 = Character([0,0], "red")

#kill player
def killPlayer(position):
    if player1.position == position:
        if player2.position == [0,0]:
            player1.position = [9,0]
        else:
            player1.position = [0,0]
    if player2.position == position:
        if player1.position == [0,9]:
            player2.position = [9,9]
        else:
            player2.position = [0,9]

# display game data on Window.
def displayBoard(board, screen):
    
    # clear the window screen
    screen.fill((0,0,0)) 
    
    #draw boarder
    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(0,0,50,600))
    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(550,0,50,600))
    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(50,0,500,50))
    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(50,550,500,50))
    
    
    
     
    for indexX, x in enumerate(board):
        for indexY, y in enumerate(x):
            if isinstance(y, Terrain):
                if y.material == 'soft':
                    pygame.draw.rect(screen, (150, 75, 0), pygame.Rect((indexY+1)*50,(indexX+1)*50,50,50))
                elif y.material == 'hard':
                    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((indexY+1)*50,(indexX+1)*50,50,50))
            if isinstance(y, Bomb):
                if y.fuse > 0:
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((indexY+1)*50,(indexX+1)*50,50,50))
                    y.fuse -= 1
                    
                    
                elif y.fuse == 0:
                    #print(y.fuse, y)
                    y.droppedBy.bombsTotal += 1
                    pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+1)*50,(indexX+1)*50,50,50))
                    
                    
                    
                    # bomb destroys everything it can
                    ''' in wrong place. Should not be in display function. Need to Move and separate graphics and grid code'''
                    
                    for explode in range(1, y.blastRadius+1):  
                        if indexX+explode < 10:
                            
                            # if player is grid kill player.
                            killPlayer([indexX+explode,indexY])
                                
                                
                            #explode down    
                            if board[indexX+explode][indexY] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+1)*50,(indexX+explode+1)*50,50,50))
                                board[indexX+explode][indexY] = 0
                            elif board[indexX+explode][indexY].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+1)*50,(indexX+explode+1)*50,50,50))
                                board[indexX+explode][indexY] = 0
                                break
                            elif board[indexX+explode][indexY].material == 'hard':
                                break
                    
                    for explode in range(1, y.blastRadius+1):      
                        if indexX-explode > -1:
                            killPlayer([indexX-explode,indexY])    
                            
                            #explode up
                            if board[indexX-explode][indexY] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+1)*50,(indexX-explode+1)*50,50,50))
                                board[indexX-explode][indexY] = 0
                            elif board[indexX-explode][indexY].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+1)*50,(indexX-explode+1)*50,50,50))
                                board[indexX-explode][indexY] = 0
                                break
                            elif board[indexX-explode][indexY].material == 'hard':
                                break
                        
                    for explode in range(1, y.blastRadius+1): 
                        #explode left
                        if indexY-explode > -1:
                            
                        # if player in grid kill player.
                            killPlayer([indexX,indexY-explode])
                            
                            if board[indexX][indexY-explode] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY-explode+1)*50,(indexX+1)*50,50,50))
                                board[indexX][indexY-explode] = 0
                            elif board[indexX][indexY-explode].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY-explode+1)*50,(indexX+1)*50,50,50))
                                board[indexX][indexY-explode] = 0
                                break
                            elif board[indexX][indexY-explode].material == 'hard':
                                break
                        
                    for explode in range(1, y.blastRadius+1):   
                        #explode right
                        if indexY+explode < 10:
                            
                            # if player is in grid ref kill player.
                            killPlayer([indexX,indexY+explode])
                           
                        
                            if board[indexX][indexY+explode] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+explode+1)*50,(indexX+1)*50,50,50))
                                board[indexX][indexY+explode] = 0
                            elif board[indexX][indexY+explode].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+explode+1)*50,(indexX+1)*50,50,50))
                                board[indexX][indexY+explode] = 0
                                break
                            elif board[indexX][indexY+explode].material == 'hard':
                                break
                                           
                    # remove bomb from board
                    board[indexX][indexY] = 0
                    
    # draw players on the screen
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((player1.position[1]+1)*50,(player1.position[0]+1)*50,50,50))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player2.position[1]+1)*50,(player2.position[0]+1)*50,50,50))



class Main:
     
    myboard = MapGrid()
    
    # list of bombs coordinates in grid. 
    bombs = []
    
    # for infinite loop. Change end to 'quit' to exit loop.
    end = 1
      
    #initiate pygame, window/screen and clock speed  
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    
    clock = pygame.time.Clock()
    
    
    # start game loop
    while end != 'quit':
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = 'quit'
                
        # capture key presses
        keypress = pygame.key.get_pressed()
        
        # do character actions acording to key presses
        playerKeys(keypress, myboard, player1, player2, bombs)
       
        # display graphics frame of board.            
        displayBoard(myboard.myboard, screen)
                
        pygame.display.flip()
        
        clock.tick(15)
