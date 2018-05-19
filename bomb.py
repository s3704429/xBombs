import pygame

class Bomb(object):
    '''
    classdocs
    '''


    def __init__(self, material, time, blastRadius, player, gridPosition):
        '''
        Constructor
        '''
        self.material = material # string
        self.fuse = time # int
        self.blastRadius = blastRadius # int
        self.droppedBy = player # 
        self.gridPosition = gridPosition # list
        self.image0 = pygame.image.load('images/bomb.png')
        self.image1 = pygame.image.load('images/bomb2.png')
        pass
    
    def getImage(self):
        if self.fuse%2 ==0:
            return self.image0
        else:
            return self.image1 
    
    def detonateBomb (self) :
        # returns 
        pass
    def checkTile (self) :
        # returns 
        pass
    def destroyTile (self) :
        # returns 
        pass
    def destroyCharacter (self) :
        # returns 
        pass
    def destroyBomb (self) :
        # returns 
        pass
    def recordScore (self) :
        # returns 
        pass   