import pygame
from character import *
from terrain import *
from bomb import *
from mapGrid import *
from playerKeys import *
from powerup import *


BOARDSIZEX = 10
BOARDSIZEY = 10
CELLSIZE = 50


# preload players
player1 = Character((BOARDSIZEX-1)*CELLSIZE, (BOARDSIZEY-1)*CELLSIZE, [9,9], "green")
player2 = Character(0,0, [0,0], "red")

# load sound and music
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
explodeSound = pygame.mixer.Sound('sound/Explosion1.wav')
p1Death = pygame.mixer.Sound('sound/sfx_deathscream_human5.wav')
p2Death = pygame.mixer.Sound('sound/sfx_deathscream_human13.wav')
pygame.mixer.music.load('sound/01 A Night Of Dizzy Spells.mp3') 

background = pygame.image.load('images/Grass_50x50.jpg')
     
      

#kill player
def killPlayer(position):
    if player1.position == position:
        p1Death.play()
        if player2.position == [0,0] or player1.position == [0,0]:
            player1.position = [BOARDSIZEX-1,0]
            player1.X = 0*CELLSIZE
            player1.Y = (BOARDSIZEX-1)*CELLSIZE
        else:
            player1.position = [0,0]
            player1.X = 0*CELLSIZE
            player1.Y = 0*CELLSIZE
    if player2.position == position:
        p2Death.play()
        if player1.position == [0,BOARDSIZEY-1] or player2.position == [0,BOARDSIZEY-1]:
            player2.position = [BOARDSIZEX-1,BOARDSIZEY-1]
            player2.X = (BOARDSIZEX-1)*CELLSIZE
            player2.Y = (BOARDSIZEY-1)*CELLSIZE
        else:
            player2.position = [0,(BOARDSIZEX-1)]
            player2.X = (BOARDSIZEX-1)*CELLSIZE
            player2.Y = 0*CELLSIZE



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
            
            if y == 0:
                screen.blit(background, (indexY*CELLSIZE,indexX*CELLSIZE))
                
            # power up display
            if isinstance(y, Powerup):
                screen.blit(pygame.image.load(y.image), (indexY*CELLSIZE,indexX*CELLSIZE))
                
            # if terrain object then display at the corresponding coordinates
            if isinstance(y, Terrain):
                if y.material == 'soft':
                    pygame.draw.rect(screen, (150, 75, 0), pygame.Rect((indexY)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                    
                elif y.material == 'hard':
                    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((indexY)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                    sprite = pygame.image.load('images/Unbreakable.jpg')
                    screen.blit(sprite, (indexY*CELLSIZE,indexX*CELLSIZE))
            # if bomb object then display at the corresponding coordinates      
            if isinstance(y, Bomb):
                # if fuse timer not zero just draw the bomb  
                if y.fuse > 0:
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((indexY)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                    y.fuse -= 1
                    
                # if the timer is 0 its time to explode bomb. Draw explosion.
                elif y.fuse == 0:
                    y.droppedBy.bombsTotal += 1
                    pygame.draw.rect(screen, (200, 200, 100), pygame.Rect((indexY)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                    explodeSound.play()
                    
                    
                    # bomb destroys everything it can
                    ''' in wrong place. Should not be in display function. Need to Move and separate graphics and grid code'''
                    
                    ''' kill player if they are in the grid they dropped the bomb '''
                    killPlayer([indexX,indexY])
                    
                    ''' explode bomb and check all grid spaces in bombs wake '''
                    
                    ''' range and bounds check'''
                    for explode in range(1, y.blastRadius+1):  
                        if indexX+explode < BOARDSIZEX:
                            
                            ''' kill player if they are in grid'''
                            # if player is grid kill player.
                            killPlayer([indexX+explode,indexY])
                                
                                
                            #explode down    
                            ''' grid empty show explode '''
                            if board[indexX+explode][indexY] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*CELLSIZE,(indexX+explode)*CELLSIZE,CELLSIZE,CELLSIZE))
                                board[indexX+explode][indexY] = 0
                            # if soft terrain then explode 
                            elif board[indexX+explode][indexY].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*CELLSIZE,(indexX+explode)*CELLSIZE,CELLSIZE,CELLSIZE))
                                
                                board[indexX+explode][indexY] = Powerup('soft',900)
                            # if a bomb, trigger bombs explosion 
                            elif board[indexX+explode][indexY].material == 'bomb':    
                                board[indexX+explode][indexY].fuse = 0
                            # if hard terrain, stop blast 
                            #elif board[indexX+explode][indexY].material == 'hard':
                                
                            
                    
                    for explode in range(1, y.blastRadius+1):      
                        if indexX-explode > -1:
                            killPlayer([indexX-explode,indexY])    
                            
                            #explode up
                            if board[indexX-explode][indexY] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*CELLSIZE,(indexX-explode)*CELLSIZE,CELLSIZE,CELLSIZE))
                                board[indexX-explode][indexY] = 0
                            elif board[indexX-explode][indexY].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY)*CELLSIZE,(indexX-explode)*CELLSIZE,CELLSIZE,CELLSIZE))
                                board[indexX-explode][indexY] = 0                                
                            elif board[indexX-explode][indexY].material == 'bomb':    
                                board[indexX-explode][indexY].fuse = 0
                            #elif board[indexX-explode][indexY].material == 'hard':
                                
                            
                        
                    for explode in range(1, y.blastRadius+1): 
                        #explode left
                        if indexY-explode > -1:
                            
                        # if player in grid kill player.
                            killPlayer([indexX,indexY-explode])
                            
                            if board[indexX][indexY-explode] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY-explode)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                                board[indexX][indexY-explode] = 0
                            elif board[indexX][indexY-explode].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY-explode)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                                board[indexX][indexY-explode] = 0
                            elif board[indexX][indexY-explode].material == 'bomb':    
                                board[indexX][indexY-explode].fuse = 0
                            #elif board[indexX][indexY-explode].material == 'hard':
                                
                            
                        
                    for explode in range(1, y.blastRadius+1):   
                        #explode right
                        if indexY+explode < BOARDSIZEY:
                            
                            # if player is in grid ref kill player.
                            killPlayer([indexX,indexY+explode])
                           
                        
                            if board[indexX][indexY+explode] == 0:
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+explode)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                                board[indexX][indexY+explode] = 0
                            elif board[indexX][indexY+explode].material == 'soft':
                                pygame.draw.rect(screen, (255, 200, 0), pygame.Rect((indexY+explode)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                                board[indexX][indexY+explode] = 0
                            elif board[indexX][indexY+explode].material == 'bomb':    
                                board[indexX][indexY+explode].fuse = 0    
                            #elif board[indexX][indexY+explode].material == 'hard':
                                
                            
                                           
                    # remove bomb from board
                    board[indexX][indexY] = 0
                    
    # draw players on the screen
    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((player1.position[1])*CELLSIZE,(player1.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player2.position[1])*CELLSIZE,(player2.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    player1.draw(screen)
    player2.draw(screen)
   # print(player1.X, ":", player1.Y, ":", (player1.position[0])*CELLSIZE, ":", (player1.position[1])*CELLSIZE, ":STAND:", player1.standing)


class Main:
     
    myboard = MapGrid()
    
    # list of bombs coordinates in grid. 
    bombs = []
    
    # for infinite loop. Change end to 'quit' to exit loop.
    end = 1
      
    
      
    #initiate pygame, window/screen and clock speed  
    pygame.init()
    screen = pygame.display.set_mode((BOARDSIZEX*CELLSIZE, BOARDSIZEY*CELLSIZE))
    
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
        
        clock.tick(30)