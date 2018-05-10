import pygame
from character import *
from terrain import *
from bomb import *
from mapGrid import *
from playerKeys import *
from powerup import *
from menu import *
from explosion import *

BOARDSIZEX = 13
BOARDSIZEY = 13
CELLSIZE = 50


# preload players
player1 = Character((BOARDSIZEX-1)*CELLSIZE, (BOARDSIZEY-1)*CELLSIZE, [BOARDSIZEX-1,BOARDSIZEY-1], "green", "Penguin")
player2 = Character(0,0, [0,0], "red", "")
player3 = Character(0,(BOARDSIZEY-1)*CELLSIZE, [0,BOARDSIZEX-1], "red", "")
player4 = Character((BOARDSIZEY-1)*CELLSIZE,0, [BOARDSIZEX-1,0], "red", "")

# load sound and music
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
explodeSound = pygame.mixer.Sound('sound/Explosion1.wav')
p1Death = pygame.mixer.Sound('sound/sfx_deathscream_human5.wav')
p2Death = pygame.mixer.Sound('sound/sfx_deathscream_human13.wav')


# Preload images

#background = pygame.image.load('images/Grass_50x50.jpg')
#boomImg = pygame.image.load('images/boom_50x50.jpg')     
backgroundFull = pygame.image.load('images/Grass_full_screen_650x650.jpg')      
unbreakable = pygame.image.load('images/Unbreakable.jpg')
breakable = pygame.image.load('images/breakable.jpg')
pBlastImg = pygame.image.load('images/powerups/blast.png')
pExtraImg = pygame.image.load('images/powerups/extrabomb.png')
pNukeImg = pygame.image.load('images/powerups/nuke.png')
pSpeedImg = pygame.image.load('images/powerups/speed.png')
pTimeImg = pygame.image.load('images/powerups/time.png')

#kill player
def killPlayer(position, bomb):
    if player1.position == position:
        p1Death.play()
        bomb.droppedBy.score += 1
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
        bomb.droppedBy.score += 1
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
    #screen.fill((0,0,0)) 
    screen.blit(backgroundFull, (0,0))
    #draw boarder
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(0,0,50,600))
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(550,0,50,600))
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(50,0,500,50))
    #pygame.draw.rect(screen, (50, 150, 50), pygame.Rect(50,550,500,50))
    
    
    
    # cycle through map grid 2d list and display what is in each cell.
    for indexX, x in enumerate(board):
        for indexY, y in enumerate(x):
            
            if y == 0:
                #screen.blit(background, (indexY*CELLSIZE,indexX*CELLSIZE))
                pass
            if isinstance(y, Fireball):
                if y.fuse >= 0:
                    screen.blit(y.image, (indexY*CELLSIZE,indexX*CELLSIZE))
                    y.animateExplosion()

                elif y.fuse < 0:
                    board[indexX][indexY] = 0
            # power up display
            if isinstance(y, Powerup):
                screen.blit(y.image, (indexY*CELLSIZE,indexX*CELLSIZE))
                
            # if terrain object then display at the corresponding coordinates
            if isinstance(y, Terrain):
                if y.material == 'soft':
                    #pygame.draw.rect(screen, (150, 75, 0), pygame.Rect((indexY)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                    screen.blit(breakable, (indexY*CELLSIZE,indexX*CELLSIZE))
                elif y.material == 'hard':
                    #pygame.draw.rect(screen, (150, 150, 150), pygame.Rect((indexY)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                    #sprite = pygame.image.load('images/Unbreakable.jpg')
                    screen.blit(unbreakable, (indexY*CELLSIZE,indexX*CELLSIZE))
            # if bomb object then display at the corresponding coordinates      
            if isinstance(y, Bomb):
                # if fuse timer not zero just draw the bomb  
                if y.fuse > 0:
                    pygame.draw.rect(screen, (200, 200, 200), pygame.Rect((indexY)*CELLSIZE,(indexX)*CELLSIZE,CELLSIZE,CELLSIZE))
                    y.fuse -= 1
                    
                # if the timer is 0 its time to explode bomb. Draw explosion.
                elif y.fuse == 0:
                    y.droppedBy.bombsTotal += 1
                    
                    explodeSound.play()
                    
                    
                    # bomb destroys everything it can
                    ''' in wrong place. Should not be in display function. Need to Move and separate graphics and grid code'''
                    
                    ''' kill player if they are in the grid they dropped the bomb '''
                    killPlayer([indexX,indexY], y)
                    
                    ''' explode bomb and check all grid spaces in bombs wake '''
                    
                    ''' range and bounds check'''
                    for explode in range(1, y.blastRadius+1):  
                        if indexX+explode < BOARDSIZEX:
                            
                            ''' kill player if they are in grid'''
                            # if player is grid kill player.
                            killPlayer([indexX+explode,indexY], y)
                                
                                
                            #explode down    
                            ''' grid empty show explode '''
                            if board[indexX+explode][indexY] == 0:
                                board[indexX+explode][indexY] = Fireball()
                            # if soft terrain then explode 
                            elif board[indexX+explode][indexY].material == 'soft':
                                # leave a power up once terrain explodes.
                                if isinstance(board[indexX+explode][indexY], Terrain):
                                    board[indexX+explode][indexY] = Fireball(board, [indexX+explode, indexY], Powerup('soft',900))
                                else:
                                    board[indexX+explode][indexY] = Fireball()
                                break
                            # if a bomb, trigger bombs explosion 
                            elif board[indexX+explode][indexY].material == 'bomb':    
                                board[indexX+explode][indexY].fuse = 0
                            # if hard terrain, stop blast 
                            elif board[indexX+explode][indexY].material == 'hard':
                                break
                            
                    
                    for explode in range(1, y.blastRadius+1):      
                        if indexX-explode > -1:
                            killPlayer([indexX-explode,indexY], y)    
                            
                            #explode up
                            if board[indexX-explode][indexY] == 0:
                                board[indexX-explode][indexY] = Fireball()
                            elif board[indexX-explode][indexY].material == 'soft':
                                if isinstance(board[indexX-explode][indexY], Terrain):
                                    board[indexX-explode][indexY] = Fireball(board, [indexX-explode,indexY],Powerup('soft',900))
                                else:
                                    board[indexX-explode][indexY] = Fireball()
                                break                                
                            elif board[indexX-explode][indexY].material == 'bomb':    
                                board[indexX-explode][indexY].fuse = 0
                            elif board[indexX-explode][indexY].material == 'hard':
                                break
                            
                        
                    for explode in range(1, y.blastRadius+1): 
                        #explode left
                        if indexY-explode > -1:
                            
                        # if player in grid kill player.
                            killPlayer([indexX,indexY-explode], y)
                            
                            
                            if board[indexX][indexY-explode] == 0:
                                board[indexX][indexY-explode] = Fireball()
                            elif board[indexX][indexY-explode].material == 'soft':
                                if isinstance(board[indexX][indexY-explode], Terrain):
                                    board[indexX][indexY-explode] = Fireball(board,[indexX,indexY-explode],Powerup('soft',900) )
                                else:
                                    board[indexX][indexY-explode] = Fireball()
                                break
                            elif board[indexX][indexY-explode].material == 'bomb':    
                                board[indexX][indexY-explode].fuse = 0
                            elif board[indexX][indexY-explode].material == 'hard':
                                break
                            
                        
                    for explode in range(1, y.blastRadius+1):   
                        #explode right
                        if indexY+explode < BOARDSIZEY:
                            
                            # if player is in grid ref kill player.
                            killPlayer([indexX,indexY+explode], y)
                           
                        
                            if board[indexX][indexY+explode] == 0:
                                #board[indexX][indexY+explode] = 0
                                board[indexX][indexY+explode] = Fireball()
                            elif board[indexX][indexY+explode].material == 'soft':
                                if isinstance(board[indexX][indexY+explode], Terrain):
                                    board[indexX][indexY+explode] = Fireball(board,[indexX,indexY+explode], Powerup('soft',900))
                                else:
                                    board[indexX][indexY+explode] = Fireball()
                                break
                            elif board[indexX][indexY+explode].material == 'bomb':    
                                board[indexX][indexY+explode].fuse = 0  
                                break  
                            elif board[indexX][indexY+explode].material == 'hard':
                                break
                            
                                           
                    # remove bomb from board
                    board[indexX][indexY] = 0
                    board[indexX][indexY] = Fireball()
                    
    # draw players on the screen
    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((player1.position[1])*CELLSIZE,(player1.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player2.position[1])*CELLSIZE,(player2.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    player1.draw(screen)
    player2.draw(screen)
    
    #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player3.position[1])*CELLSIZE,(player3.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    #player3.draw(screen)
    #player4.draw(screen)
   # print(player1.X, ":", player1.Y, ":", (player1.position[0])*CELLSIZE, ":", (player1.position[1])*CELLSIZE, ":STAND:", player1.standing)


class Main:
    
    mapNumber = 0
     
    
    
    # list of bombs coordinates in grid. 
    bombs = []
    
    # for infinite loop. Change end to 'quit' to exit loop.
    end = 1
    endMap = 1  
    
      
    #initiate pygame, window/screen and clock speed  
    pygame.init()
    screen = pygame.display.set_mode((BOARDSIZEX*CELLSIZE, BOARDSIZEY*CELLSIZE))
    pygame.display.set_caption('xBombs')
    clock = pygame.time.Clock()
    keypress = pygame.key.get_pressed()
    
    scores = ""
    
    font = pygame.font.SysFont('Comic Sans MS', 54)
    font2 = pygame.font.SysFont('Comic Sans MS', 45)
    
    pygame.mixer.music.load('sound/Azureflux_-_01_-_BOMB.mp3')
    pygame.mixer.music.play()
    
    #load menu screen
    while end != 'quit':
        # end loop variable, change to quit to exit
        endMap = 0
        
        # create text for menu
        textsurface = font2.render(('Press 1 to 3 for map. p to quit.'), False, (100, 200, 100))
        
        #display menu image and text
        screen.blit(backgroundFull,(0,0))
        screen.blit(pygame.image.load('images/xBomb_img_clr.png'),(0,0))
        screen.blit(textsurface,(100,450))
        textsurface = font2.render("Player 1: " + str(player1.score), False, (150, 0, 0))
        screen.blit(textsurface,(275,500))
        textsurface = font2.render("Player 2: " + str(player2.score), False, (20, 20, 200))
        screen.blit(textsurface,(275,550))
        
        # get keys pressed
        keypress = pygame.key.get_pressed()
        
        #load game with map according to keypressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = 'quit'
            if keypress[pygame.K_1]:
                mapNumber = 1
                pygame.mixer.music.load('sound/01 A Night Of Dizzy Spells.mp3') 
            if keypress[pygame.K_2]:
                mapNumber = 2
                pygame.mixer.music.load('sound/Eric_Skiff_-_03_-_Chibi_Ninja.mp3') 
            if keypress[pygame.K_3]:
                mapNumber = 3
                pygame.mixer.music.load('sound/Eric_Skiff_-_10_-_Arpanauts.mp3') 
            if keypress[pygame.K_p]:
                end = 'quit'
            
        # refresh screen    
        pygame.display.update()
        
        # if a map is selected then load game with that map
        if mapNumber != 0:
            myboard = MapGrid(mapNumber)
                
            # start the music
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(5)
          
    
            # start game loop
            while endMap != 'quit':
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end = 'quit'
                        endMap = 'quit'
                    # quit game by pressing p
                    if keypress[pygame.K_p]:
                        mapNumber = 0
                        endMap = 'quit'
                
                
                        
                # capture key presses
                keypress = pygame.key.get_pressed()
                
                # do character actions acording to key presses
                playerKeys(keypress, myboard, (player1, player2), bombs)
               
                
                    
               
                # display graphics frame of board.
                displayBoard(myboard.myboard, screen)
                        
                pygame.display.update()
                
                clock.tick(30) 
                
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sound/Azureflux_-_01_-_BOMB.mp3')
            pygame.mixer.music.play(5)