import cmath
import numpy
import sys
from PIL import Image
from random import randint
from math import *

class mazeDFS:
    def __init__(self,inputMazeDimensions):
        self.mazeDimensions = inputMazeDimensions
        self.mazeArray = numpy.zeros((self.mazeDimensions[0],self.mazeDimensions[1],3));
    def dfsMazeAlgorithm(self,startMazePosition):
        self.mazeArray[startMazePosition[0]][startMazePosition[1]][2] = 1
        while(self.isAnyPath(startMazePosition)):
            nextCell = self.randomizePath(startMazePosition)
            #print(nextCell)
            self.mazeArray[startMazePosition[0]][startMazePosition[1]][2] = 1;
            self.mazeArray[startMazePosition[0]+nextCell[0]][startMazePosition[1]+nextCell[1]] = numpy.array((-nextCell[0],-nextCell[1],1));
            self.dfsMazeAlgorithm((startMazePosition[0]+nextCell[0],startMazePosition[1]+nextCell[1]))
    def isVisited(self,checkPosition):
        return self.mazeArray[checkPosition[0]][checkPosition[1]][2]
    def isCellAvilable(self,checkPosition):
        if(self.isCellInMaze(checkPosition) and self.isVisited(checkPosition) == 0):
            return True
        else:
            return False
    def isAnyPath(self,checkPosition):
        howManyPaths = 0
        if(self.isCellAvilable((checkPosition[0] - 1,checkPosition[1]))):
            howManyPaths += 1
        if(self.isCellAvilable((checkPosition[0] + 1,checkPosition[1]))):
            howManyPaths += 1
        if(self.isCellAvilable((checkPosition[0],checkPosition[1] + 1))):
            howManyPaths += 1
        if(self.isCellAvilable((checkPosition[0],checkPosition[1] - 1))):
            howManyPaths += 1
        return howManyPaths
    def randomizePath(self,checkPosition):
        randomPath = randint(0, self.isAnyPath(checkPosition)-1)
        #print(randomPath)
        howManyPaths = -1
        if(self.isCellAvilable((checkPosition[0] - 1,checkPosition[1]))):
            howManyPaths += 1
            if(randomPath == howManyPaths):
                return (-1,0)
        if(self.isCellAvilable((checkPosition[0] + 1,checkPosition[1]))):
            howManyPaths += 1
            if(randomPath == howManyPaths):
                return (1,0)
        if(self.isCellAvilable((checkPosition[0],checkPosition[1] + 1))):
            howManyPaths += 1
            if(randomPath == howManyPaths):
                return (0,1)
        if(self.isCellAvilable((checkPosition[0],checkPosition[1] - 1))):
            howManyPaths += 1
            if(randomPath == howManyPaths):
                return (0,-1)
        #print("to nie dziala")
    def isCellInMaze(self,checkPosition):
        if(checkPosition[0]>=0 and checkPosition[0]<self.mazeDimensions[0]):
            if(checkPosition[1]>=0 and checkPosition[1]<self.mazeDimensions[1]):
                return True
            else:
                return False
        else:
            return False
    def mazePrintingArray(self):
        self.arrayToPrint = numpy.zeros((2*self.mazeDimensions[0]+1,2*self.mazeDimensions[1]+1))
        for i in range(2*self.mazeDimensions[0]+1):
            for j in range(2*self.mazeDimensions[1]+1):
                if(i%2==0 or j%2==0):
                    self.arrayToPrint[i][j] = 1
        for i in range(self.mazeDimensions[0]):
            for j in range(self.mazeDimensions[1]):
                self.arrayToPrint[2*i+1+int(self.mazeArray[i][j][0])][2*j+1+int(self.mazeArray[i][j][1])] = 0
    def createMazeImage(self):
        self.arrayToPNG = numpy.zeros((2*self.mazeDimensions[0]+1,2*self.mazeDimensions[1]+1,3), numpy.uint8)
        for i in range(2*self.mazeDimensions[0]+1):
            for j in range(2*self.mazeDimensions[1]+1):
                self.arrayToPNG[i][j] = numpy.array([k*(not self.arrayToPrint[i][j]) for k in [255,255,255]])
    def saveImage(self):
        sys.setrecursionlimit(self.mazeDimensions[0]*self.mazeDimensions[1])
        self.dfsMazeAlgorithm((1,1))
        self.mazePrintingArray()
        self.createMazeImage()
        generatedMazeImage = Image.fromarray(self.arrayToPNG, "RGB")
        generatedMazeImage.save("mazeImage.png")
maze = mazeDFS((200,200))
maze.saveImage()
