from terrain import *

BOARDSIZEX = 13
BOARDSIZEY = 13

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
                
        for numLoop in range(BOARDSIZEX):
            self.myboard.append([0,0,0,0,0,0,0,0,0,0,0,0,0])
            
        
        
        # load terrain to board
        
        # terrain map objects - co-ordinates - Aarons example map from Assignment 2
        hard = [[0,4],[0,5],[1,1],[1,2],[1,7],[1,8],[2,1],[2,4],[2,5],[2,8],[4,2],[4,4],[4,5],[4,7],[4,9],
               [5,0],[5,2],[5,4],[5,5],[5,7],[5,9],[7,1],[7,4],[7,5],[7,8],[8,1],[8,2],[8,7],[8,8],[9,4],[9,5]]
        
        soft = [[0,2],[0,7],[1,4],[1,5],[2,0],[2,3],[2,6],[2,9],[3,2],[3,7],[4,1],[4,8],[5,1],[5,8],[6,2],[6,7],
                [7,0],[7,3],[7,6],[7,9],[8,4],[8,5],[9,2],[9,7]]
        
        
        # load terrain to board
        for each in hard:
            self.myboard[each[0]][each[1]] = Terrain("hard")
        
        for each in soft:
            self.myboard[each[0]][each[1]] = Terrain("soft")
                
    
    # get the object in the grid reference
    def getGridObject(self, position, x, y):
        return self.myboard[position[0]+y][position[1]+x]
        
    # clear the objet in the grid reference
    def removeObject(self, position):
        self.myboard[position[0]][position[1]]
        return 1