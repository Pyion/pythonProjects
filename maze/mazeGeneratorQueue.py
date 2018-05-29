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
        self.cellBeforeArr = numpy.zeros((self.mazeDimensions[0],self.mazeDimensions[1],2))
        self.initMazeArray()
        self.avilableCells = numpy.ones(self.mazeDimensions)
        self.initBfs(startPosition)

    def initMazeArray(self):
        for i in range(self.mazePrintDimensions[0]):
            for j in range(self.mazePrintDimensions[1]):
                if(i%2 == 0 or j%2 == 0):
                    self.mazeArray[i][j] = 1

    def initBfs(self,startBfsPosition):
        self.cellQueue.put((startBfsPosition,[2*i+1 for i in startBfsPosition],startBfsPosition))
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
                self.cellQueue.put(((queryCell[0]+1,queryCell[1]),(2*queryCell[0]+2,2*queryCell[1]+1),queryCell))
            if(self.isCell((queryCell[0]-1,queryCell[1])) and i==1):
                self.cellQueue.put(((queryCell[0]-1,queryCell[1]),(2*queryCell[0],2*queryCell[1]+1),queryCell))
            if(self.isCell((queryCell[0],queryCell[1]+1)) and i==2):
                self.cellQueue.put(((queryCell[0],queryCell[1]+1),(2*queryCell[0]+1,2*queryCell[1]+2),queryCell))
            if(self.isCell((queryCell[0],queryCell[1]-1)) and i==3):
                self.cellQueue.put(((queryCell[0],queryCell[1]-1),(2*queryCell[0]+1,2*queryCell[1]),queryCell))

    def bfsMazeAlgorithm(self):
        while(not self.cellQueue.empty()):
            currentCell, fillCell, cellBefore = self.cellQueue.get()
            print(currentCell)
            if(self.avilableCells[currentCell[0]][currentCell[1]]):
                #print(currentCell)
                self.mazeArray[fillCell[0]][fillCell[1]] = 0
                self.avilableCells[currentCell[0]][currentCell[1]] = 0
                self.cellBeforeArr[currentCell[0]][currentCell[1]] = cellBefore
                self.checkCells(currentCell)

    def createMazeImage(self):
        self.arrayToPNG = numpy.zeros((self.mazePrintDimensions[0],self.mazePrintDimensions[1],3), numpy.uint8)
        for i in range(self.mazePrintDimensions[0]):
            for j in range(self.mazePrintDimensions[1]):
                self.arrayToPNG[i][j] = numpy.array([k*(not self.mazeArray[i][j]) for k in [255,255,255]])

    def createPath(self,endCell):
        currentCell = endCell
        #print("cell:",currentCell)
        while(list(self.cellBeforeArr[currentCell[0]][currentCell[1]]) != currentCell):
            #print("cell: ",currentCell)
            self.arrayToPNG[2*currentCell[0]+1][2*currentCell[1]+1] = numpy.array([255,0,0],numpy.uint8)
            currentCell = self.cellBeforeArr[currentCell[0]][currentCell[1]]
            currentCell = [int(i) for i in currentCell]
            #print("cell:  ",currentCell)

    def saveImage(self):
        self.createMazeImage()
        generatedMazeImage = Image.fromarray(self.arrayToPNG, "RGB")
        generatedMazeImage.save("queueMazeImage.png")
        self.createPath((self.mazeDimensions[0]-1,self.mazeDimensions[1]-1))
        generatedMazeImage = Image.fromarray(self.arrayToPNG, "RGB")
        generatedMazeImage.save("queueMazeImagePath.png")

maze = mazeBFS((15,15),(0,0))
maze.saveImage()
