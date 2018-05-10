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


class Character():


    def __init__(self, y, x, position, colour, character):
       
        self.char1WalkDown = [pygame.image.load('images/' + character + 'DOWNstill.png'), pygame.image.load('images/' + character + 'DOWNstill.png'),pygame.image.load('images/' + character + 'DOWNrightfoot.png'), pygame.image.load('images/' + character + 'DOWNrightfoot.png'), pygame.image.load('images/' + character + 'DOWNrightfoot.png'), pygame.image.load('images/' + character + 'DOWNstill.png'), pygame.image.load('images/' + character + 'DOWNstill.png'), pygame.image.load('images/' + character + 'DOWNleftfoot.png'), pygame.image.load('images/' + character + 'DOWNleftfoot.png'),pygame.image.load('images/' + character + 'DOWNleftfoot.png')]
        self.char1WalkUp = [pygame.image.load('images/' + character + 'UPstill.png'), pygame.image.load('images/' + character + 'UPstill.png'),pygame.image.load('images/' + character + 'UPrightfoot.png'), pygame.image.load('images/' + character + 'UPrightfoot.png'), pygame.image.load('images/' + character + 'UPrightfoot.png'), pygame.image.load('images/' + character + 'UPstill.png'), pygame.image.load('images/' + character + 'UPstill.png'), pygame.image.load('images/' + character + 'UPleftfoot.png'), pygame.image.load('images/' + character + 'UPleftfoot.png'), pygame.image.load('images/' + character + 'UPleftfoot.png')]
        self.char1WalkLeft = [pygame.image.load('images/' + character + 'LEFTstill.png'), pygame.image.load('images/' + character + 'LEFTstill.png'),pygame.image.load('images/' + character + 'LEFTrightfoot.png'), pygame.image.load('images/' + character + 'LEFTrightfoot.png'), pygame.image.load('images/' + character + 'LEFTrightfoot.png'), pygame.image.load('images/' + character + 'LEFTstill.png'), pygame.image.load('images/' + character + 'LEFTstill.png'), pygame.image.load('images/' + character + 'LEFTleftfoot.png'), pygame.image.load('images/' + character + 'LEFTleftfoot.png'), pygame.image.load('images/' + character + 'LEFTleftfoot.png')]
        self.char1WalkRight = [pygame.image.load('images/' + character + 'RIGHTstill.png'), pygame.image.load('images/' + character + 'RIGHTstill.png'),pygame.image.load('images/' + character + 'RIGHTrightfoot.png'), pygame.image.load('images/' + character + 'RIGHTrightfoot.png'), pygame.image.load('images/' + character + 'RIGHTrightfoot.png'), pygame.image.load('images/' + character + 'RIGHTstill.png'), pygame.image.load('images/' + character + 'RIGHTstill.png'), pygame.image.load('images/' + character + 'RIGHTleftfoot.png'), pygame.image.load('images/' + character + 'RIGHTleftfoot.png'), pygame.image.load('images/' + character + 'RIGHTleftfoot.png')]

        
        self.status = "alive" # string
        self.position = position # list
        self.colour = colour # string
        self.score = 0 # int
        self.bombsTotal = 3 # int
        self.bombStrength = 2 # int
        self.fuse = 90 
        
        self.powerUps = [0] # list
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
            myboard.myboard[self.position[0]][self.position[1]] = Bomb('soft', self.fuse, self.bombStrength, self, self.position)
            bombs.append(self.position);
            self.bombsTotal -= 1
        
    