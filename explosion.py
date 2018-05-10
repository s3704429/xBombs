# class for explosion graphics
import pygame


class Fireball(object):
    '''
    classdocs
    '''


    def __init__(self, board=0, gridCoord=0, powerup=0):
        
        
        self.gridCoord = gridCoord
        self.powerup = powerup
        self.board = board
        '''
        Constructor
        '''
        self.material = "explosion" # string
        self.fuse = 14 # int
        #self.droppedBy = player # 
        #self.gridPosition = gridPosition # list
        self.frame = 0
        
        self.animate = [pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast.png'),
                        pygame.image.load('images/explode/blast1.png'),
                        pygame.image.load('images/explode/blast1.png'),
                        pygame.image.load('images/explode/blast2.png'),
                        pygame.image.load('images/explode/blast2.png'),
                        #pygame.image.load('images/explode/blast2.png'),
                        pygame.image.load('images/explode/blast3.png'),
                        pygame.image.load('images/explode/blast3.png'),
                        #pygame.image.load('images/explode/blast3.png'),
                        #pygame.image.load('images/explode/blast1.png'),
                        #pygame.image.load('images/explode/blast1.png'),
                        #pygame.image.load('images/explode/blast1.png')]
                        ]
        
        self.image = self.animate[self.frame]
        pass
    
    
    
    
    def animateExplosion(self):
        if self.fuse == 0 and self.gridCoord != 0:
            self.board[self.gridCoord[0]][self.gridCoord[1]] = self.powerup
        if self.frame == 13:
            self.fuse -= 1
            self.image = self.animate[self.frame]
            self.frame = 0
        else:
            self.frame += 1
            self.fuse -= 1
            self.image = self.animate[self.frame]
        
    
        