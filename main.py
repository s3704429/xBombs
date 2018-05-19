import pygame
import time
import random

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

playerCharacters = [Character((BOARDSIZEX-1)*CELLSIZE, (BOARDSIZEY-1)*CELLSIZE, [-1,-1], "green", "Penguin"),
                      Character(0,0, [-1,-1], "red", "snowman"), Character(0,(BOARDSIZEY-1)*CELLSIZE, [-1,-1], "red", ""),
                      Character((BOARDSIZEY-1)*CELLSIZE,0, [-1,-1], "red", "chick")]


i,j,k,l = 0,0,0,0

player1 = playerCharacters[0]
player2 = playerCharacters[1]
player3 = playerCharacters[2]
player4 = playerCharacters[3]

winner = 0


# load sound and music
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.mixer.init()
explodeSound = pygame.mixer.Sound('sound/Explosion1.wav')
xBombSound = pygame.mixer.Sound('sound/sfx_exp_long4.wav')
p1Death = pygame.mixer.Sound('sound/sfx_deathscream_human5.wav')
p2Death = pygame.mixer.Sound('sound/sfx_deathscream_human13.wav')
p3Death = pygame.mixer.Sound('sound/sfx_deathscream_human10.wav')
p4Death = pygame.mixer.Sound('sound/sfx_deathscream_human2.wav')

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

bombImages = [pygame.image.load('images/bomb.png'), pygame.image.load('images/bomb2.png')]

#kill player
def killPlayer(position, bomb):
    if player1.position == position:
        p1Death.play()
        if bomb.droppedBy != player1:
            bomb.droppedBy.score += 1
        else:
            bomb.droppedBy.score -= 1
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
        if bomb.droppedBy != player2:
            bomb.droppedBy.score += 1
        else:
            bomb.droppedBy.score -= 1
            
        if player1.position == [0,BOARDSIZEY-1] or player2.position == [0,BOARDSIZEY-1]:
            player2.position = [BOARDSIZEX-1,BOARDSIZEY-1]
            player2.X = (BOARDSIZEX-1)*CELLSIZE
            player2.Y = (BOARDSIZEY-1)*CELLSIZE
        else:
            player2.position = [0,(BOARDSIZEX-1)]
            player2.X = (BOARDSIZEX-1)*CELLSIZE
            player2.Y = 0*CELLSIZE
    if player3.position == position:
        p3Death.play()
        
        if bomb.droppedBy != player3:
            bomb.droppedBy.score += 1
        else:
            bomb.droppedBy.score -= 1
        
        if player4.position == [0,BOARDSIZEY-1] or player3.position == [0,BOARDSIZEY-1]:
            player3.position = [BOARDSIZEX-1,BOARDSIZEY-1]
            player3.X = (BOARDSIZEX-1)*CELLSIZE
            player3.Y = (BOARDSIZEY-1)*CELLSIZE
        else:
            player3.position = [0,(BOARDSIZEX-1)]
            player3.X = (BOARDSIZEX-1)*CELLSIZE
            player3.Y = 0*CELLSIZE
    if player4.position == position:
        p4Death.play()
        
        if bomb.droppedBy != player4:
            bomb.droppedBy.score += 1
        else:
            bomb.droppedBy.score -= 1
        
        if player3.position == [0,BOARDSIZEY-1] or player4.position == [0,BOARDSIZEY-1]:
            player4.position = [BOARDSIZEX-1,0]
            player4.X = 0*CELLSIZE
            player4.Y = (BOARDSIZEX-1)*CELLSIZE
        else:
            player4.position = [0,0]
            player4.X = 0*CELLSIZE
            player4.Y = 0*CELLSIZE


''' Explodes the bomb as far as its range. Check what is in the path and destroys it. Or stops '''
def explodeBomb(board, bomb, x, y, explode):
    
    if bomb.material == "xbomb":
        if explode[0] < 0:              # -1 , -1
            explode[1] += explode[0]
        elif explode[0] > 0:            # 1 , 1
            explode[1] += explode[0]
        elif explode[1] < 0:            # 1  ,  -1
            explode[0] -= explode[1]
        elif explode[1] > 0:            #  -1  , 1
            explode[0] -= explode[1]
            
    ''' kill player if they are in grid'''
    # if player is grid kill player.
    killPlayer([x+explode[0],y+explode[1]], bomb)
        
    #explode     
    ''' grid empty show explode '''
    if 0 <= x+explode[0] <= 12 and 0 <= y+explode[1] <= 12:
        if board[x+explode[0]][y+explode[1]] == 0:
            board[x+explode[0]][y+explode[1]] = Fireball()
        # if soft terrain then explode 
        elif board[x+explode[0]][y+explode[1]].material == 'soft':
            # leave a power up once terrain explodes.
            if isinstance(board[x+explode[0]][y+explode[1]], Terrain):
                powerUpDrop = random.randint(0,2)
                if powerUpDrop==0:
                    board[x+explode[0]][y+explode[1]] = Fireball(board, (x+explode[0],y+explode[1]), Powerup('soft',900))
                    if bomb.material != "xbomb": 
                        return 'stop'
                else:
                    board[x+explode[0]][y+explode[1]] = Fireball()
                    if bomb.material != "xbomb": 
                        return 'stop'
            else:
                board[x+explode[0]][y+explode[1]] = Fireball()
                if bomb.material != "xbomb": 
                    return 'stop'
        # if a bomb, trigger bombs explosion 
        elif board[x+explode[0]][y+explode[1]].material == 'bomb':    
            board[x+explode[0]][y+explode[1]].fuse = 0
            if bomb.material != "xbomb": 
                return 'stop'
        # if hard terrain, stop blast 
        elif board[x+explode[0]][y+explode[1]].material == 'hard':
            if bomb.material != "xbomb": 
                return 'stop'


# display game data on Window.
def displayBoard(board, screen, totalPlayers):
    
    # clear the window screen
    screen.fill((0,0,0)) 
    screen.blit(backgroundFull, (0,0))
    
    # cycle through map grid 2d list and display what is in each cell.
    for indexX, x in enumerate(board):
        for indexY, y in enumerate(x):
            
            if y == 0:
                #screen.blit(background, (indexY*CELLSIZE,indexX*CELLSIZE))
                pass
            elif isinstance(y, Fireball):
                if y.fuse >= 0:
                    screen.blit(y.image, (indexY*CELLSIZE,indexX*CELLSIZE))
                    y.animateExplosion()

                elif y.fuse < 0:
                    board[indexX][indexY] = 0
            # power up display
            elif isinstance(y, Powerup):
                screen.blit(y.powerupImage, (indexY*CELLSIZE,indexX*CELLSIZE))
                
            # if terrain object then display at the corresponding coordinates
            elif isinstance(y, Terrain):
                if y.material == 'soft':
                    screen.blit(breakable, (indexY*CELLSIZE,indexX*CELLSIZE))
                elif y.material == 'hard':
                    screen.blit(unbreakable, (indexY*CELLSIZE,indexX*CELLSIZE))
            
            # if bomb object then display at the corresponding coordinates      
            elif isinstance(y, Bomb):
                # if fuse timer not zero just draw the bomb  
                if y.fuse > 0:                    
                    if y.fuse%2 ==0:
                        screen.blit(bombImages[0], (indexY*CELLSIZE,indexX*CELLSIZE))
                    else:
                        screen.blit(bombImages[1], (indexY*CELLSIZE,indexX*CELLSIZE))
                    y.fuse -= 1
                    
                # if the timer is 0 its time to explode bomb. Draw explosion.
                elif y.fuse == 0:
                    y.droppedBy.bombsTotal += 1
                   
                   #play bomb sound
                    if y.material == 'xbomb':
                        xBombSound.play()
                    else: 
                        explodeSound.play()
                    # bomb destroys everything it can
                    ''' in wrong place. Should not be in display function. Need to Move and separate graphics and grid code'''
                    ''' kill player if they are in the grid they dropped the bomb '''
                    killPlayer([indexX,indexY], y)
                    
                    ''' explode bomb and check all grid spaces in bombs wake '''
                    ''' Explode Down - range and bounds check'''
                    for explode in range(1, y.blastRadius+1):  
                        if indexX+explode < BOARDSIZEX:
                            if explodeBomb(board,y,indexX,indexY,[explode,0]) == 'stop': 
                                break
                    ''' Explode Up'''
                    for explode in range(1, y.blastRadius+1):      
                        if indexX-explode > -1:
                            if explodeBomb(board,y,indexX,indexY,[-explode,0]) == 'stop':
                                break
                            
                    ''' Explode Left '''    
                    for explode in range(1, y.blastRadius+1): 
                        #explode left
                        if indexY-explode > -1:
                            if explodeBomb(board,y,indexX,indexY,[0,-explode]) == 'stop':
                                break
                    ''' Explode Right '''    
                    for explode in range(1, y.blastRadius+1):   
                        #explode right
                        if indexY+explode < BOARDSIZEY:
                            if explodeBomb(board,y,indexX,indexY,[0,explode]) == 'stop':
                                break
                                           
                    # remove bomb from board
                    board[indexX][indexY] = 0
                    board[indexX][indexY] = Fireball()
                    
    # draw players on the screen
    #pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((player1.position[1])*CELLSIZE,(player1.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player2.position[1])*CELLSIZE,(player2.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    player1.draw(screen)

    if totalPlayers > 1:
        player2.draw(screen)
    
    #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect((player3.position[1])*CELLSIZE,(player3.position[0])*CELLSIZE,CELLSIZE,CELLSIZE))
    if totalPlayers > 2: 
        player3.draw(screen)
    if totalPlayers == 4:
        player4.draw(screen)
   # print(player1.X, ":", player1.Y, ":", (player1.position[0])*CELLSIZE, ":", (player1.position[1])*CELLSIZE, ":STAND:", player1.standing)


class Main:
    
    # for infinite loop. Change end to 'quit' to exit loop.
    end = 1
    endMap = 1     
    numberOfPlayers = 2
    
    # list of bombs coordinates in grid.
    bombs = []
    mapNumber = 0
      
    #initiate pygame, window/screen and clock speed  
    pygame.init()
    screen = pygame.display.set_mode((BOARDSIZEX*CELLSIZE, BOARDSIZEY*CELLSIZE))
    pygame.display.set_caption('xBombs')
    clock = pygame.time.Clock()
    keypress = pygame.key.get_pressed()

    scores = ""
    
    font = pygame.font.SysFont('comicsansms', 40)
    font2 = pygame.font.SysFont('comicsansms', 25)
    font3 = pygame.font.SysFont('comicsansms', 55)
    
    pygame.mixer.music.load('sound/Azureflux_-_01_-_BOMB.mp3')
    pygame.mixer.music.play()
    
    time.sleep(7.9)
    
    textsurface = font.render(('theCoolNamePendingGroup'), False, (255, 255, 255))
    screen.blit(textsurface,(50,300))
    pygame.display.update()
    time.sleep(4)
    textsurface = font.render(('Presents'), False, (255, 255, 255))
    screen.blit(textsurface,(200,350))
    pygame.display.update()
    time.sleep(3.3)

    pygame.key.set_repeat() 
    
    #load menu screen
    while end != 'quit':
        # end loop variable, change to quit to exit
        endMap = 0

        # get keys pressed
        keypress = pygame.key.get_pressed()
        
        clock.tick(10) 

        if keypress[pygame.K_a]:
            if numberOfPlayers < len(playerCharacters):
                numberOfPlayers += 1
            else:
                numberOfPlayers = 1
         
        
        if keypress[pygame.K_KP0]:
            if i <= len(playerCharacters)-1:
                global player1 
                player1 = playerCharacters[i]
                i += 1
            else:
                i = 0
        if keypress[pygame.K_q]:
            if j <= len(playerCharacters)-1:
                global player2 
                player2 = playerCharacters[j]
                j += 1
            else:
                j = 0
        if keypress[pygame.K_y]:
            if k <= len(playerCharacters)-1:
                global player3 
                player3 = playerCharacters[k]
                k += 1
            else:
                k = 0
        if keypress[pygame.K_KP7]:
            if l <= len(playerCharacters)-1:
                global player4 
                player4 = playerCharacters[l]
                l += 1
            else:
                l = 0
        
        # create text for menu
        
        #display menu image and text
        screen.blit(backgroundFull,(0,0))
        
        textsurface = font2.render(('Press 1 to 3 = start map.     p = quit.'), False, (100, 200, 100))
        screen.blit(textsurface,(100,450))
        
        
        if winner == 0:
            screen.blit(pygame.image.load('images/xBomb_img_clr.png'),(0,0))
        else:
            winnerImage = pygame.transform.scale(winner[0].char1WalkDown[0], (275, 300))
            screen.blit(winnerImage,(200,100))
            textsurface = font3.render(('WINNER: Player ' + str(winner[1]+1)), False, (255, 255, 255))
            screen.blit(textsurface,(75,50))
           
            
        
        textsurface = font2.render(('a = add players'), False, (100, 200, 100))
        screen.blit(textsurface,(100,475))
        textsurface = font2.render(('players trigger = change character'), False, (100, 200, 100))
        screen.blit(textsurface,(100,500))
        textsurface = font2.render("Player 1: " + str(player1.score), False, (150, 0, 0))
        screen.blit(textsurface,(15,530))
        screen.blit(player1.char1WalkDown[0],(80,560))
        if numberOfPlayers > 1:
            textsurface = font2.render("Player 2: " + str(player2.score), False, (20, 20, 200))
            screen.blit(player2.char1WalkDown[0],(230,560))
            screen.blit(textsurface,(200,530))
        
        if numberOfPlayers > 2:
            textsurface = font2.render("Player 3: " + str(player3.score), False, (150, 0, 0))
            screen.blit(textsurface,(365,530))
            screen.blit(player3.char1WalkDown[0],(390,560))
        if numberOfPlayers == 4:
            textsurface = font2.render("Player 4: " + str(player4.score), False, (20, 20, 200))
            screen.blit(player4.char1WalkDown[0],(540,560))
            screen.blit(textsurface,(515,530))
        
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
 
            player1 = Character((BOARDSIZEX-1)*CELLSIZE, (BOARDSIZEY-1)*CELLSIZE, [BOARDSIZEX-1,BOARDSIZEY-1], "green", player1.character)
            
            players = [player1]
            if numberOfPlayers > 1:
                player2 = Character(0,0, [0,0], "red", player2.character)
                players.append(player2)
            if numberOfPlayers > 2:
                player3 = Character(0,(BOARDSIZEY-1)*CELLSIZE, [0,BOARDSIZEX-1], "red", player3.character)
                players.append(player3)
            if numberOfPlayers == 4:
                player4 = Character((BOARDSIZEY-1)*CELLSIZE,0, [BOARDSIZEX-1,0], "red", player4.character)
                players.append(player4)
            
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

                    for int in range(0, len(players)):
                        if players[int].score >= 10:
                            winner = [players[int],int]
                            mapNumber = 0
                            endMap = 'quit'

                        
                # capture key presses
                keypress = pygame.key.get_pressed()
                
                # do character actions acording to key presses

                playerKeys(keypress, myboard, players, bombs)
               
                # display graphics frame of board.
                displayBoard(myboard.myboard, screen, len(players))

                        
                pygame.display.update()
                
                clock.tick(30) 
                
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sound/Azureflux_-_01_-_BOMB.mp3')
            pygame.mixer.music.play(5)
