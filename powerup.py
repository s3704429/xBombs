import pygame
import random
from mapGrid import *

#from main import * 

class Powerup(object):
    '''
    classdocs
    '''


    def __init__(self, material, time):
        
        randomSelection = random.randint(1,10)
        '''
        Constructor
        '''
        if randomSelection <= 3:
            self.material = material # string
            self.fuse = time # int
            self.powerupImage = pygame.image.load('images/powerups/blast.png')
            self.selectedPowerup = "blastRadiusUp"
        elif randomSelection == 4:
            self.material = material # string
            self.fuse = time # int
            self.powerupImage = pygame.image.load('images/powerups/speed.png')
            self.selectedPowerup = "speedUp"
        elif randomSelection >= 6 and randomSelection <= 8:
            self.material = material # string
            self.fuse = time # int
            self.powerupImage = pygame.image.load('images/powerups/extrabomb.png')
            self.selectedPowerup = "bombTotalUp"
        elif randomSelection == 5:
            self.material = material # string
            self.fuse = time # int
            self.powerupImage = pygame.image.load('images/powerups/nuke.png')
            self.selectedPowerup = "nuke"
        elif randomSelection == 9:
            self.material = material # string
            self.fuse = time # int
            self.powerupImage = pygame.image.load('images/powerups/time.png')
            self.selectedPowerup = "time"
        elif randomSelection == 10:
            # items
            randomItem = random.randint(1,9)
        
            if randomItem <= 2:
                self.material = material # string
                self.fuse = time # int
                self.powerupImage = pygame.image.load('images/powerups/hammer.png')
                self.selectedPowerup = "hammer"
                self.count = 3 # how many times it can be used
            elif randomItem >= 3 and randomItem <= 4:
                self.material = material # string
                self.fuse = time # int
                self.powerupImage = pygame.image.load('images/powerups/steelHammer.png')
                self.selectedPowerup = "steelHammer"
                self.count = 3 # how many times it can be used
            elif randomItem >= 5 and randomItem <= 6:
                self.material = material # string
                self.fuse = time # int
                self.powerupImage = pygame.image.load('images/powerups/remoteDetonator.png')
                self.selectedPowerup = "remote"
                self.count = 3 # how many times it can be used
            elif randomItem >= 7 and randomItem <= 8:
                self.material = material # string
                self.fuse = time # int
                self.powerupImage = pygame.image.load('images/powerups/springBomb.png')
                self.selectedPowerup = "springBomb"
                self.count = 3 # how many times it can be used
            elif randomItem == 9:
                self.material = material # string
                self.fuse = time # int
                self.powerupImage = pygame.image.load('images/powerups/xbomb.png')
                self.selectedPowerup = "xBomb"

    def drop_powerup(screen, x,y):
        pass
	    #blastImage = pygame.image.load('images/blast.png')

    def blast(x,y):

        screen.blit(powerupImage, (x,y))

	#blast(x,y)
    
    def grabPowerup(self, player):
        if self.selectedPowerup == "blastRadiusUp":
            player.bombStrength += 1
        elif self.selectedPowerup == "speedUp":
            player.speed += 2
        elif self.selectedPowerup == "bombTotalUp":
            player.bombsTotal += 1
        elif self.selectedPowerup == "nuke":
            player.bombStrength = 13
        elif self.selectedPowerup == "time":
            player.fuse = 45    
        
        # items
        elif self.selectedPowerup == "hammer":
            player.item = self
        elif self.selectedPowerup == "steelHammer":
            player.item = self
        elif self.selectedPowerup == "remote":
            player.item = self
            player.fuse = 900
        elif self.selectedPowerup == "springBomb":
            player.item = self
        elif self.selectedPowerup == "xBomb":
            player.item = self
        
#drop_powerup(screen, (indexY)*CELLSIZE,(indexX-explode)*CELLSIZE)


    
