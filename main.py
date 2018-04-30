import pygame
from character import *
from terrain import *
from bomb import *
from mapGrid import *
from playerKeys import *


BOARDSIZEX = 10
BOARDSIZEY = 10
CELLSIZE = 50


# preload players
player1 = Character(9*50, 9*50, [9,9], "green")
player2 = Character(0,0, [0,0], "red")

# load sound and music
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
explodeSound = pygame.mixer.Sound('sound/Explosion1.wav')
p1Death = pygame.mixer.Sound('sound/sfx_deathscream_human5.wav')
p2Death = pygame.mixer.Sound('sound/sfx_deathscream_human13.wav')
pygame.mixer.music.load('sound/01 A Night Of Dizzy Spells.mp3') 


     
      

#kill player
def killPlayer(position):
    if player1.position == position:
        p1Death.play()
        if player2.position == [0,0] or player1.position == [0,0]:
            player1.position = [9,0]
            player1.X = 0*50
            player1.Y = 9*50
        else:
            player1.position = [0,0]
            player1.X = 0*50
            player1.Y = 0*50
    if player2.position == position:
        p2Death.play()
        if player1.position == [0,9] or player2.position == [0,9]:
            player2.position = [9,9]
            player2.X = 9*50
            player2.Y = 9*50
        else:
            player2.position = [0,9]
            player2.X = 9*50
            player2.Y = 0*50

# display game data on Window.
def displayBoard(board, screen):
    
    # clear the window screen
    screen.fill((0,0,0)) 
    
    #draw boarder
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(0,0,50,600))
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(550,0,50,600))
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(50,0,500,50))
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(50,550,500,50))
    
    
    
    # cycle through map grid 2d list and display what is in each cell.
    for indexX, x in enumerate(board):
        for indexY, y in enumerate(x):
            
            # if terrain object then display at the corresponding coordinates
            if isinstance(y, Terrain):
                if y.material == 'soft':
                    pygame.draw.rect(screen, (150, 75, 0), pygame.Rect((indexY)*50,(indexX)*50,50,50))
                elif y.material == 'hard':
                    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((indexY)*50,(indexX)*50,50,50))
                    
            # if bomb object then display at the corresponding coordinates      
            if isinstance(y, Bomb):
                # if fuse timer not zero just draw the bomb  
                if y.fuse > 0:
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((indexY)*50,(indexX)*50,50,50))
                    y.fuse -= 1
                    
                # if the timer is 0 its time to explode bomb. Draw explosion.
                elif y.fuse == 0:
                    y.droppedBy.bombsTotal += 1
                    pygame.draw.rect(screen, (200, 200, 100), pygame.Rect((indexY)*50,(indexX)*50,50,50))
                    explodeSound.play()
                    
                    
                    # bomb destroys everything it can
                    ''' in wrong place. Should not be in display function. Need to Move and separate graphics and grid code'''
                    killPlayer([indexX,indexY])
                    for explode in range(1, y.blastRadius+1):  
                        if indexX+explode < 10:
                            
                            # if player is grid kill player.
                            killPlayer([indexX+explode,indexY])
                                
                                
                            #explode down    
                            if board[indexX+explode][indexY] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*50,(indexX+explode)*50,50,50))
                                board[indexX+explode][indexY] = 0
                            elif board[indexX+explode][indexY].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*50,(indexX+explode)*50,50,50))
                                board[indexX+explode][indexY] = 0
                            elif board[indexX+explode][indexY].material == 'bomb':
                                board[indexX+explode][indexY].fuse = 0
                            elif board[indexX+explode][indexY].material == 'hard':
                                break
                    
                    for explode in range(1, y.blastRadius+1):      
                        if indexX-explode > -1:
                            killPlayer([indexX-explode,indexY])    
                            
                            #explode up
                            if board[indexX-explode][indexY] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*50,(indexX-explode)*50,50,50))
                                board[indexX-explode][indexY] = 0
                            elif board[indexX-explode][indexY].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*50,(indexX-explode)*50,50,50))
                                board[indexX-explode][indexY] = 0
                            elif board[indexX-explode][indexY].material == 'bomb':    
                                board[indexX-explode][indexY].fuse = 0
                            elif board[indexX-explode][indexY].material == 'hard':
                                break
                        
                    for explode in range(1, y.blastRadius+1): 
                        #explode left
                        if indexY-explode > -1:
                            
                        # if player in grid kill player.
                            killPlayer([indexX,indexY-explode])
                            
                            if board[indexX][indexY-explode] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY-explode)*50,(indexX)*50,50,50))
                                board[indexX][indexY-explode] = 0
                            elif board[indexX][indexY-explode].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY-explode)*50,(indexX)*50,50,50))
                                board[indexX][indexY-explode] = 0
                            elif board[indexX][indexY-explode].material == 'bomb':    
                                board[indexX][indexY-explode].fuse = 0
                            elif board[indexX][indexY-explode].material == 'hard':
                                break
                        
                    for explode in range(1, y.blastRadius+1):   
                        #explode right
                        if indexY+explode < 10:
                            
                            # if player is in grid ref kill player.
                            killPlayer([indexX,indexY+explode])
                           
                        
                            if board[indexX][indexY+explode] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+explode)*50,(indexX)*50,50,50))
                                board[indexX][indexY+explode] = 0
                            elif board[indexX][indexY+explode].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+explode)*50,(indexX)*50,50,50))
                                board[indexX][indexY+explode] = 0
                            elif board[indexX][indexY+explode].material == 'bomb':
                                board[indexX][indexY+explode].fuse = 0   
                            elif board[indexX][indexY+explode].material == 'hard':
                                break
                                           
                    # remove bomb from board
                    board[indexX][indexY] = 0
                    
    # draw players on the screen
    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((player1.position[1])*50,(player1.position[0])*50,50,50))
    #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player2.position[1])*50,(player2.position[0])*50,50,50))
    player1.draw(screen)
    player2.draw(screen)
    print(player1.X, ":", player1.Y, ":", (player1.position[0])*50, ":", (player1.position[1])*50, ":STAND:", player1.standing)


class Main:
     
    myboard = MapGrid()
    
    # list of bombs coordinates in grid. 
    bombs = []
    
    # for infinite loop. Change end to 'quit' to exit loop.
    end = 1
      
    
      
    #initiate pygame, window/screen and clock speed  
    pygame.init()
    screen = pygame.display.set_mode([BOARDSIZEX*CELLSIZE, BOARDSIZEY*CELLSIZE])
    
    # start the music
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(5)
  
    
    
    
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
                
        pygame.display.update()
        
        clock.tick(24)
