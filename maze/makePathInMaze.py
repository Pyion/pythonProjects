import cmath
from numpy import *
from queue import *
from PIL import Image
from random import randint,shuffle
from math import *


class makePath:
    def __init__(self,mazePngFile):
        self.mazeArray = array(Image.open(mazePngFile))
        self.mazeDimensions = [i//2 for i in self.mazeArray.shape[:2]]
        self.vertexQueue = PriorityQueue()
        self.isOut = zeros(self.mazeDimensions)
        
        self.cellBefore = [[[]]*self.mazeDimensions[0]]*self.mazeDimensions[1]
        self.trackLength = array([[4*self.mazeDimensions[0]*self.mazeDimensions[1]]*self.mazeDimensions[0]]*self.mazeDimensions[1])
    def dijkstraInit(self,startCell):
        self.vertexQueue.put((0,startCell))
        self.trackLength[startCell[0]][startCell[1]] = 0
        self.nodesInit()
        self.dijkstra()

    def nodesInit(self):
        self.nodes = [[]] * self.mazeDimensions[0]
        self.nodes = [self.nodes] * self.mazeDimensions[1]
        for i in range(self.mazeDimensions[0]):
            for j in range(self.mazeDimensions[1]):
                self.nodesOfCell((i,j))
                print(self.nodes[i][j])

    def nodesOfCell(self,inputCell):
        if(self.cellInMaze(inputCell,(inputCell[0]+1,inputCell[1]))):
            self.nodes[inputCell[0]][inputCell[1]].append((inputCell[0]+1,inputCell[1]))
        if(self.cellInMaze(inputCell,(inputCell[0]-1,inputCell[1]))):
            self.nodes[inputCell[0]][inputCell[1]].append((inputCell[0]-1,inputCell[1]))
        if(self.cellInMaze(inputCell,(inputCell[0],inputCell[1]+1))):
            self.nodes[inputCell[0]][inputCell[1]].append((inputCell[0],inputCell[1]+1))
        if(self.cellInMaze(inputCell,(inputCell[0],inputCell[1]-1))):
            self.nodes[inputCell[0]][inputCell[1]].append((inputCell[0],inputCell[1]-1))

    def cellInMaze(self,startPosition,checkPosition):
        if(checkPosition[0]>=0 and checkPosition[0]<self.mazeDimensions[0]):
            if(checkPosition[1]>=0 and checkPosition[1]<self.mazeDimensions[1]):
                if(self.mazeArray[startPosition[0]+checkPosition[0]+1][startPosition[1]+checkPosition[1]].all() != self.mazeArray[0][0].all()):
                    return True
        return False

    def dijkstra(self):
        while(not self.vertexQueue.empty()):
            currentValue, currentCell = self.vertexQueue.get()
            print(currentCell)
            for currentNodeCell in self.nodes[currentCell[0]][currentCell[1]]:
                if(self.isOut[currentNodeCell[0]][currentNodeCell[1]] == 0):
                    #self.vertexQueue.put(((currentNodeCell[0]),(currentNodeCell[1])))
                    if(self.trackLength[currentNodeCell[0]][currentNodeCell[1]]>self.trackLength[currentCell[0]][currentCell[1]]+2):
                            self.vertexQueue.put((self.trackLength[currentCell[0]][currentCell[1]]+2,(currentNodeCell)))
                            self.cellBefore[currentNodeCell[0]][currentNodeCell[1]] = currentCell
                            self.trackLength[currentNodeCell[0]][currentNodeCell[1]] = self.trackLength[currentCell[0]][currentCell[1]]+2
            self.isOut[currentCell[0]][currentCell[1]] = 1
a = makePath("queueMazeImage.png")
a.dijkstraInit((0,0))
print(a.cellBefore)
print(a.trackLength)
print(a.nodes[0][0])
