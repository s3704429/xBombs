import pygame
import random

#from main import * 

class Powerup(object):
    '''
    classdocs
    '''


    def __init__(self, material, time):
        
        randomSelection = random.randint(1,9)
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

#drop_powerup(screen, (indexY)*CELLSIZE,(indexX-explode)*CELLSIZE)
