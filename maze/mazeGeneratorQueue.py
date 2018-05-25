import cmath
import numpy
import queue
from PIL import Image
from random import randint,shuffle
from math import *

class mazeBFS:
    def __init__(self,inputMazeDimensions,startPosition):
        self.cellQueue = queue.LifoQueue()
        self.mazeDimensions = inputMazeDimensions
        self.mazePrintDimensions = [2*a+1 for a in self.mazeDimensions]
        self.mazeArray = numpy.zeros(self.mazePrintDimensions)
        self.initMazeArray()
        self.avilableCells = numpy.ones(self.mazeDimensions)
        self.initBfs(startPosition)

    def initMazeArray(self):
        for i in range(self.mazePrintDimensions[0]):
            for j in range(self.mazePrintDimensions[1]):
                if(i%2 == 0 or j%2 == 0):
                    self.mazeArray[i][j] = 1

    def initBfs(self,startBfsPosition):
        self.cellQueue.put((startBfsPosition,[2*i+1 for i in startBfsPosition]))
        self.bfsMazeAlgorithm()

    def isCell(self,queryCell):
        if(self.isCellInMaze(queryCell)):
            if(self.avilableCells[queryCell[0]][queryCell[1]] == 1):
                return True
            else:
                return False
        else:
            return False

    def isCellInMaze(self,checkPosition):
        if(checkPosition[0]>=0 and checkPosition[0]<self.mazeDimensions[0]):
            if(checkPosition[1]>=0 and checkPosition[1]<self.mazeDimensions[1]):
                return True
            else:
                return False
        else:
            return False

    def checkCells(self,queryCell):
        sequenceList = [i for i in range(4)]
        shuffle(sequenceList)
        for i in sequenceList:
            if(self.isCell((queryCell[0]+1,queryCell[1])) and i==0):
                self.cellQueue.put(((queryCell[0]+1,queryCell[1]),(2*queryCell[0]+2,2*queryCell[1]+1)))
            if(self.isCell((queryCell[0]-1,queryCell[1])) and i==1):
                self.cellQueue.put(((queryCell[0]-1,queryCell[1]),(2*queryCell[0],2*queryCell[1]+1)))
            if(self.isCell((queryCell[0],queryCell[1]+1)) and i==2):
                self.cellQueue.put(((queryCell[0],queryCell[1]+1),(2*queryCell[0]+1,2*queryCell[1]+2)))
            if(self.isCell((queryCell[0],queryCell[1]-1)) and i==3):
                self.cellQueue.put(((queryCell[0],queryCell[1]-1),(2*queryCell[0]+1,2*queryCell[1])))

    def bfsMazeAlgorithm(self):
        while(not self.cellQueue.empty()):
            currentCell, fillCell = self.cellQueue.get()
            print(currentCell)
            if(self.avilableCells[currentCell[0]][currentCell[1]]):
                #print(currentCell)
                self.mazeArray[fillCell[0]][fillCell[1]] = 0
                self.avilableCells[currentCell[0]][currentCell[1]] = 0
                self.checkCells(currentCell)

    def createMazeImage(self):
        self.arrayToPNG = numpy.zeros((self.mazePrintDimensions[0],self.mazePrintDimensions[1],3), numpy.uint8)
        for i in range(self.mazePrintDimensions[0]):
            for j in range(self.mazePrintDimensions[1]):
                self.arrayToPNG[i][j] = numpy.array([k*(not self.mazeArray[i][j]) for k in [255,255,255]])

    def saveImage(self):
        self.createMazeImage()
        generatedMazeImage = Image.fromarray(self.arrayToPNG, "RGB")
        generatedMazeImage.save("queueMazeImage.png")

maze = mazeBFS((50,50),(0,0))
maze.saveImage()
