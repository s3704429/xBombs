import pygame
import random

#from main import * 

class Powerup(object):
    '''
    classdocs
    '''


    def __init__(self, material, time):
        
        num = random.randint(1,9)
        '''
        Constructor
        '''
        if num <= 3:
            self.material = material # string
            self.fuse = time # int
            self.image = pygame.image.load('images/powerups/blast.png')
            self.powerup = "blast"
        elif num == 4:
            self.material = material # string
            self.fuse = time # int
            self.image = pygame.image.load('images/powerups/speed.png')
            self.powerup = "speed"
        elif num >= 6 and num <= 8:
            self.material = material # string
            self.fuse = time # int
            self.image = pygame.image.load('images/powerups/extrabomb.png')
            self.powerup = "extrabomb"
        elif num == 5:
            self.material = material # string
            self.fuse = time # int
            self.image = pygame.image.load('images/powerups/nuke.png')
            self.powerup = "nuke"
        elif num == 9:
            self.material = material # string
            self.fuse = time # int
            self.image = pygame.image.load('images/powerups/time.png')
            self.powerup = "time"

    def drop_powerup(screen, x,y):
        pass
	    #blastImage = pygame.image.load('images/blast.png')

    def blast(x,y):

        screen.blit(blastImage, (x,y))

	#blast(x,y)
    
    def grabPowerup(self, player):
        if self.powerup == "blast":
            player.bombStrength += 1
        elif self.powerup == "speed":
            player.speed += 2
        elif self.powerup == "extrabomb":
            player.bombsTotal += 1
        elif self.powerup == "nuke":
            player.bombStrength = 13
        elif self.powerup == "time":
            player.fuse = 45    

#drop_powerup(screen, (indexY)*CELLSIZE,(indexX-explode)*CELLSIZE)
