import pygame
import random
from bomb import *

# characterWidth = CELLSIZE 
# characterHeight = CELLSIZE
characterSpeed = 3
CELLSIZE = 50

char1WalkDown = [pygame.image.load('images/DOWNstill.png'), pygame.image.load('images/DOWNstill.png'),pygame.image.load('images/DOWNrightfoot.png'), pygame.image.load('images/DOWNrightfoot.png'), pygame.image.load('images/DOWNrightfoot.png'), pygame.image.load('images/DOWNstill.png'), pygame.image.load('images/DOWNstill.png'), pygame.image.load('images/DOWNleftfoot.png'), pygame.image.load('images/DOWNleftfoot.png'),pygame.image.load('images/DOWNleftfoot.png')]
char1WalkUp = [pygame.image.load('images/UPstill.png'), pygame.image.load('images/UPstill.png'),pygame.image.load('images/UPrightfoot.png'), pygame.image.load('images/UPrightfoot.png'), pygame.image.load('images/UPrightfoot.png'), pygame.image.load('images/UPstill.png'), pygame.image.load('images/UPstill.png'), pygame.image.load('images/UPleftfoot.png'), pygame.image.load('images/UPleftfoot.png'), pygame.image.load('images/UPleftfoot.png')]
char1WalkLeft = [pygame.image.load('images/LEFTstill.png'), pygame.image.load('images/LEFTstill.png'),pygame.image.load('images/LEFTrightfoot.png'), pygame.image.load('images/LEFTrightfoot.png'), pygame.image.load('images/LEFTrightfoot.png'), pygame.image.load('images/LEFTstill.png'), pygame.image.load('images/LEFTstill.png'), pygame.image.load('images/LEFTleftfoot.png'), pygame.image.load('images/LEFTleftfoot.png'), pygame.image.load('images/LEFTleftfoot.png')]
char1WalkRight = [pygame.image.load('images/RIGHTstill.png'), pygame.image.load('images/RIGHTstill.png'),pygame.image.load('images/RIGHTrightfoot.png'), pygame.image.load('images/RIGHTrightfoot.png'), pygame.image.load('images/RIGHTrightfoot.png'), pygame.image.load('images/RIGHTstill.png'), pygame.image.load('images/RIGHTstill.png'), pygame.image.load('images/RIGHTleftfoot.png'), pygame.image.load('images/RIGHTleftfoot.png'), pygame.image.load('images/RIGHTleftfoot.png')]
           
        

class Character():


    def __init__(self, x, y, position, colour):
       
        self.status = "alive" # string
        self.position = position # list
        self.colour = colour # string
        self.score = 0 # int
        self.bombsTotal = 1 # int
        self.bombStrength = 3 # int
        
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
                window.blit(char1WalkDown[self.walkCount], (self.X,self.Y))
                self.walkCount += 1            
            elif self.up:
                window.blit(char1WalkUp[self.walkCount], (self.X,self.Y))            
                self.walkCount += 1              
            elif self.left:
                window.blit(char1WalkLeft[self.walkCount], (self.X,self.Y))            
                self.walkCount += 1
            elif self.right:
                window.blit(char1WalkRight[self.walkCount], (self.X,self.Y))            
                self.walkCount += 1  
        else:
            if self.down:
                window.blit(char1WalkDown[0], (self.X,self.Y))
                self.walkCount += 1            
            elif self.up:
                window.blit(char1WalkUp[0], (self.X,self.Y))            
                self.walkCount += 1              
            elif self.left:
                window.blit(char1WalkLeft[0], (self.X,self.Y))            
                self.walkCount += 1
            elif self.right:
                window.blit(char1WalkRight[0], (self.X,self.Y))            
                self.walkCount += 1  
            
        
    def moveUp(self, myboard):
        
        if self.Y <= (self.position[0]*50): 
            if self.position[0] > 0 and myboard.getGridObject(self.position, 0, -1) == 0:
                self.position[0] -= 1
            
        if self.Y > (self.position[0])*50:
            self.Y -= self.speed # characterSpeed

            self.standing = False
            self.down = False
            self.up = True
            self.left = False
            self.right = False
            
    def moveDown(self, myboard):
        if self.Y >= (self.position[0]*50): 
            if self.position[0] < 9 and myboard.getGridObject(self.position, 0, 1) == 0:
                self.position[0] += 1
         
        if self.Y < (self.position[0])*50:  
            self.Y += self.speed # characterSpeed
    
            self.standing = False
            self.down = True
            self.up = False
            self.left = False
            self.right = False
    
    def moveLeft(self, myboard):
        
        if self.X <= (self.position[1]*50):  
            if self.position[1] > 0 and myboard.getGridObject(self.position, -1, 0) == 0:
                self.position[1] -= 1
            
        if self.X > (self.position[1])*50:
            self.X -= self.speed # characterSpeed     
    
            self.standing = False
            self.down = False
            self.up = False
            self.left = True
            self.right = False      
    
    def moveRight(self, myboard):
        
        if self.X >= (self.position[1]*50): 
            if self.position[1] < 9 and myboard.getGridObject(self.position, 1, 0) == 0:
                self.position[1] += 1
    
        if self.X < (self.position[1])*50:
            self.X += self.speed # characterSpeed

            self.standing = False
            self.down = False
            self.up = False
            self.left = False
            self.right = True       
    
    def dropBomb(self, myboard, bombs):
        if myboard.myboard[self.position[0]][self.position[1]] == 0 and self.bombsTotal > 0:
           myboard.myboard[self.position[0]][self.position[1]] = Bomb('soft', 90, self.bombStrength, self, self.position)
           bombs.append(self.position);
           self.bombsTotal -= 1
    
