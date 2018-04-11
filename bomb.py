'''
Created on 7 Apr. 2018

@author: bob
'''

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
        pass
    
    
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