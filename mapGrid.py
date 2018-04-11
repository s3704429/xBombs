'''
Created on 11 Apr. 2018

@author: bob
'''
from src.first.terrain import Terrain


class MapGrid(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        # initiate grid via list of lists
        self.myboard = []
                
        for numLoop in range(10):
            self.myboard.append([0,0,0,0,0,0,0,0,0,0])
        
        # load terrain to board
        self.myboard[1][1] = Terrain("soft")  
        self.myboard[1][2] = Terrain("soft") 
        self.myboard[1][3] = Terrain("hard")       
        self.myboard[1][4] = Terrain("hard")
        self.myboard[1][6] = Terrain("soft")
        self.myboard[1][7] = Terrain("hard")
        self.myboard[1][8] = Terrain("soft")
        self.myboard[8][8] = Terrain("soft")
        self.myboard[2][1] = Terrain("hard")
        self.myboard[2][4] = Terrain("hard")
        self.myboard[3][1] = Terrain("hard")
        self.myboard[3][8] = Terrain("soft")
        self.myboard[4][3] = Terrain("hard")
        self.myboard[4][4] = Terrain("hard")
        self.myboard[5][1] = Terrain("soft")
        self.myboard[6][8] = Terrain("soft")
        self.myboard[7][8] = Terrain("soft")
    
    
    # get the object in the grid reference
    def getGridObject(self, position, x, y):
        return self.myboard[position[0]+y][position[1]+x]
        
    # clear the objet in the grid reference
    def removeObject(self, position):
        self.myboard[position[0]][position[1]]
        return 1