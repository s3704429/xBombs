import pygame
import random
from bomb import *
from powerup import *


# characterWidth = CELLSIZE 
# characterHeight = CELLSIZE
BOARDSIZEX = 13
BOARDSIZEY = 13

characterSpeed = 3
CELLSIZE = 50


class Character(object):


    def __init__(self, y, x, position, colour, character):
       
        self.char1WalkDown = [pygame.image.load('images/characters/' + character + 'DOWNstill.png'), pygame.image.load('images/characters/' + character + 'DOWNstill.png'),pygame.image.load('images/characters/' + character + 'DOWNrightfoot.png'), pygame.image.load('images/characters/' + character + 'DOWNrightfoot.png'), pygame.image.load('images/characters/' + character + 'DOWNrightfoot.png'), pygame.image.load('images/characters/' + character + 'DOWNstill.png'), pygame.image.load('images/characters/' + character + 'DOWNstill.png'), pygame.image.load('images/characters/' + character + 'DOWNleftfoot.png'), pygame.image.load('images/characters/' + character + 'DOWNleftfoot.png'),pygame.image.load('images/characters/' + character + 'DOWNleftfoot.png')]
        self.char1WalkUp = [pygame.image.load('images/characters/' + character + 'UPstill.png'), pygame.image.load('images/characters/' + character + 'UPstill.png'),pygame.image.load('images/characters/' + character + 'UPrightfoot.png'), pygame.image.load('images/characters/' + character + 'UPrightfoot.png'), pygame.image.load('images/characters/' + character + 'UPrightfoot.png'), pygame.image.load('images/characters/' + character + 'UPstill.png'), pygame.image.load('images/characters/' + character + 'UPstill.png'), pygame.image.load('images/characters/' + character + 'UPleftfoot.png'), pygame.image.load('images/characters/' + character + 'UPleftfoot.png'), pygame.image.load('images/characters/' + character + 'UPleftfoot.png')]
        self.char1WalkLeft = [pygame.image.load('images/characters/' + character + 'LEFTstill.png'), pygame.image.load('images/characters/' + character + 'LEFTstill.png'),pygame.image.load('images/characters/' + character + 'LEFTrightfoot.png'), pygame.image.load('images/characters/' + character + 'LEFTrightfoot.png'), pygame.image.load('images/characters/' + character + 'LEFTrightfoot.png'), pygame.image.load('images/characters/' + character + 'LEFTstill.png'), pygame.image.load('images/characters/' + character + 'LEFTstill.png'), pygame.image.load('images/characters/' + character + 'LEFTleftfoot.png'), pygame.image.load('images/characters/' + character + 'LEFTleftfoot.png'), pygame.image.load('images/characters/' + character + 'LEFTleftfoot.png')]
        self.char1WalkRight = [pygame.image.load('images/characters/' + character + 'RIGHTstill.png'), pygame.image.load('images/characters/' + character + 'RIGHTstill.png'),pygame.image.load('images/characters/' + character + 'RIGHTrightfoot.png'), pygame.image.load('images/characters/' + character + 'RIGHTrightfoot.png'), pygame.image.load('images/characters/' + character + 'RIGHTrightfoot.png'), pygame.image.load('images/characters/' + character + 'RIGHTstill.png'), pygame.image.load('images/characters/' + character + 'RIGHTstill.png'), pygame.image.load('images/characters/' + character + 'RIGHTleftfoot.png'), pygame.image.load('images/characters/' + character + 'RIGHTleftfoot.png'), pygame.image.load('images/characters/' + character + 'RIGHTleftfoot.png')]

        self.character =  character

        self.status = "alive" # string
        self.position = position # list
        self.colour = colour # string
        self.score = 0 # int
        self.bombsTotal = 1 # int
        self.itemDeploy = 0
        self.bombStrength = 1 # int
        self.fuse = 90 
        
        self.item = 0
        self.material = 'soft' # string
        self.controlKeys = None # list
        self.characterImages = None # list
        
        self.X = x
        self.Y = y
        self.speed = characterSpeed # int
        self.walkCount = 0
        self.standing = True
        self.down = True
        self.up = False
        self.left = False
        self.right = False


        self.xpos = random.randint(0,12)*CELLSIZE
        self.ypos = random.randint(0,12)*CELLSIZE
        
        pass
    
    '''
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.speed = 10
            self.walkCount = 0
        self.standing = True
        self.down = True
        self.up = False
        self.left = False
        self.right = False
    '''
            
    
    def charaterDeath (self) :
        # returns 
        pass

    def getX(self):
        return self.position[0]
    
    def getY(self):
        return self.position[1]
    
    def draw(self, window):
        if self.walkCount + 1 > 9:
            self.walkCount = 0

        if not (self.standing):
            if self.down:
                window.blit(self.char1WalkDown[self.walkCount], (self.X,self.Y))
                self.walkCount += 1            
            elif self.up:
                window.blit(self.char1WalkUp[self.walkCount], (self.X,self.Y))            
                self.walkCount += 1              
            elif self.left:
                window.blit(self.char1WalkLeft[self.walkCount], (self.X,self.Y))            
                self.walkCount += 1
            elif self.right:
                window.blit(self.char1WalkRight[self.walkCount], (self.X,self.Y))            
                self.walkCount += 1  
        else:
            if self.down:
                window.blit(self.char1WalkDown[0], (self.X,self.Y))
                self.walkCount += 1            
            elif self.up:
                window.blit(self.char1WalkUp[0], (self.X,self.Y))            
                self.walkCount += 1              
            elif self.left:
                window.blit(self.char1WalkLeft[0], (self.X,self.Y))            
                self.walkCount += 1
            elif self.right:
                window.blit(self.char1WalkRight[0], (self.X,self.Y))            
                self.walkCount += 1  
            
        
    def moveUp(self, myboard):
        if self.Y <= (self.position[0]*CELLSIZE)-30: 
            if self.position[0] > 0 and myboard.getGridObject(self.position, 0, -1) == 0:
                self.position[0] -= 1
        if self.position[0] > 0 and myboard.getGridObject(self.position, 0, -1) != 0 and self.Y < (self.position[0])*CELLSIZE-31: 
            if isinstance(myboard.getGridObject(self.position, 0, -1), Powerup):
                myboard.getGridObject(self.position, 0, -1).grabPowerup(self)
                myboard.removeObject(self.position,0,-1)
            pass    
        if self.Y > ((self.position[0])*CELLSIZE)-40:
            self.Y -= self.speed # characterSpeed

        self.standing = False
        self.down = False
        self.up = True
        self.left = False
        self.right = False
            
    def moveDown(self, myboard):
        if self.Y >= (self.position[0]*CELLSIZE+10): 
            if self.position[0] < BOARDSIZEY-1 and myboard.getGridObject(self.position, 0, 1) == 0:
                self.position[0] += 1
        if self.position[0] < BOARDSIZEY-1 and myboard.getGridObject(self.position, 0, 1) != 0 and self.Y > (self.position[0])*CELLSIZE-5:    
            if isinstance(myboard.getGridObject(self.position, 0, 1), Powerup):
                myboard.getGridObject(self.position, 0, 1).grabPowerup(self)
                myboard.removeObject(self.position,0,1)   
            pass
        elif self.Y < (self.position[0])*CELLSIZE+11:
            self.Y += self.speed # characterSpeed
        
        self.standing = False
        self.down = True
        self.up = False
        self.left = False
        self.right = False
        
    def moveLeft(self, myboard):
        
        if self.X <= (self.position[1]*CELLSIZE)-20:  
            if self.position[1] > 0 and myboard.getGridObject(self.position, -1, 0) == 0:
                self.position[1] -= 1
        if self.position[1] > 0 and myboard.getGridObject(self.position, -1, 0) != 0 and self.X < (self.position[1])*CELLSIZE-5:    
            if isinstance(myboard.getGridObject(self.position, -1, 0), Powerup):
                myboard.getGridObject(self.position,  -1, 0).grabPowerup(self)
                myboard.removeObject(self.position, -1, 0)
            pass
        elif self.X > (self.position[1])*CELLSIZE-20:
            self.X -= self.speed # characterSpeed     
    
        self.standing = False
        self.down = False
        self.up = False
        self.left = True
        self.right = False      
    
    def moveRight(self, myboard):
        
        if self.X >= (self.position[1]*CELLSIZE)+20: 
            if self.position[1] < BOARDSIZEX-1 and myboard.getGridObject(self.position, 1, 0) == 0:
                self.position[1] += 1
        if self.position[1] < BOARDSIZEX-1 and myboard.getGridObject(self.position, 1, 0) != 0 and self.X > (self.position[1])*CELLSIZE+5:    
            if isinstance(myboard.getGridObject(self.position, 1, 0), Powerup):
                myboard.getGridObject(self.position,  1, 0).grabPowerup(self)
                myboard.removeObject(self.position, 1, 0)
            pass
        elif self.X < (self.position[1])*CELLSIZE+20:
            self.X += self.speed # characterSpeed

        self.standing = False
        self.down = False
        self.up = False
        self.left = False
        self.right = True       
    
    def dropBomb(self, myboard, bombs):
        if myboard.myboard[self.position[0]][self.position[1]] == 0 and self.bombsTotal > 0:
            myboard.myboard[self.position[0]][self.position[1]] = Bomb('bomb', self.fuse, self.bombStrength, self, self.position)
            bombs.append(self.position);
            self.bombsTotal -= 1
        
    #use items code section
    
    def useItem(self, board, x,y):
        
        if self.item.selectedPowerup == "hammer" and self.item.count > 0:
            if isinstance(board.getGridObject(self.position, x, y), Terrain):
                if board.getGridObject(self.position, x, y).material == 'soft':
                    board.removeObject(self.position, x, y)
                    self.item.count -= 1
        elif self.item.selectedPowerup == "steelHammer"  and self.item.count > 0:
            if isinstance(board.getGridObject(self.position, x, y), Terrain):
                board.removeObject(self.position, x, y)
                self.item.count -= 1
        elif self.item.selectedPowerup == "remote" and self.item.count > 0:
            
            for indexX in range(13):
                for indexY in range(0,13):
                    # if bomb object then display at the corresponding coordinates      
                    if isinstance(board.getGridObject([indexX,indexY], 0, 0), Bomb):
                        # if fuse timer not zero just draw the bomb
                        if board.getGridObject([indexX,indexY], 0, 0).droppedBy == self:
                            if self.item.count > 1:
                                self.item.count -= 1
                            else:
                                self.item = 0
                                self.fuse = 90
                            board.getGridObject([indexX,indexY], 0, 0).fuse = 0
                            
               
        elif self.item.selectedPowerup == "springBomb"and self.item.count > 0:
            
            f = 1
            
            for num in range(1,13):
                if self.bombsTotal != 0:
                    if self.position[0]+(y*num) < 13 and self.position[1]+(x*num) < 13 and f != 0: 
                        if self.position[0]+(y*num) > -1 and self.position[1]+(x*num) > -1: 
                            if board.getGridObject(self.position, x*num, y*num) == 0:
                                board.myboard[self.position[0]+(y*num)][self.position[1]+(x*num)] = Bomb('bomb', self.fuse, self.bombStrength, self, [0,0])
                                self.bombsTotal -= 1
                                self.itemDeploy = 15
                                self.item.count -= 1
                                f = 0
                            
                                
                        
            
        elif self.item.selectedPowerup == "xBomb":
            board.myboard[self.position[0]][self.position[1]] = Bomb('xbomb', self.fuse, self.bombStrength, self, [0,0])
            
    