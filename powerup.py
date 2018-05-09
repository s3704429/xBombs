import pygame
import random

#from main import * 

class Powerup(object):
    '''
    classdocs
    '''

    def __init__(self, material, time):
        '''
        Constructor
        '''
        self.material = material # string
        self.fuse = time # int

        randomSelection=random.randint(0,2)
        if randomSelection==0:
            self.image = 'images/blast.png'
            self.selectedPowerup="blastRadiusUp"
        elif randomSelection==1:
            self.image = 'images/extrabomb.png'
            self.selectedPowerup="bombTotalUp"
        elif randomSelection==2:
            self.image = 'images/speed.png'
            self.selectedPowerup="speedUp"
        # etc for the rest of the powerups (limits of RNG will need to be 
        # incresed/decreased depending on how many there are)

    def blast(x,y):

        screen.blit(powerupImage, (x,y))

    
    # when player picksup run this function.
    def grabPowerup(self, player):
        if self.selectedPowerup=="blastRadiusUp":
            player.bombStrength += 1
        elif self.selectedPowerup=="bombTotalUp":
            player.bombsTotal += 1
        elif self.selectedPowerup=="speedUp":
            player.speed += 1
