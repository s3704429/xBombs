import pygame

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
        self.image = 'images/blast.png'

    def drop_powerup(screen, x,y):

	    blastImage = pygame.image.load('images/blast.png')

    def blast(x,y):

        screen.blit(blastImage, (x,y))

	#blast(x,y)

#drop_powerup(screen, (indexY)*CELLSIZE,(indexX-explode)*CELLSIZE)
