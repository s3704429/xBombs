'''
Created on 7 Apr. 2018

@author: bob
'''

class Character():
    '''
    classdocs
    '''


    def __init__(self, position, colour):
       
        self.status = "alive" # string
        self.position = position # list
        self.colour = colour # string
        self.score = 0 # int
        self.bombsTotal = 1 # int
        self.bombStrength = 1 # int
        self.speed = 1 # int
        self.powerUps = [0] # list
        self.material = 'soft' # string
        self.controlKeys = None # list
        self.characterImages = None # list
        pass
            
    
    def charaterDeath (self) :
        # returns 
        pass