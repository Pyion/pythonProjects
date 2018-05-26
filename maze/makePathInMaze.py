import cmath
import numpy
import queue
from PIL import Image
from random import randint,shuffle
from math import *

class priorityQueue:
    def __init__(self):
        self.queueList = [0]
        self.size = 0

    def get(self):
        if(len(self.queueList) > 0):
            self.pop()
            return self.queueList[0]
        else:
            return False

    def push(self, value):
        self.queueList.append(value)
        self.size += 1
        currentIndicator = self.size
        while(self.queueList[currentIndicator//2]>value and currentIndicator//2 > 0):
            self.queueList[currentIndicator] = self.queueList[currentIndicator//2]
            self.queueList[currentIndicator//2] = value
            currentIndicator //=2

    def pop(self):
        self.queueList[1] = self.queueList[self.size]
        self.queueList.pop()
        self.size -=1
        indicator = 1
        while(2*indicator <= self.size):
            indicator = self.popStep(indicator)
    def popStep(self,indicator):
        if(self.queueList[indicator] > self.queueList[2*indicator]):
            self.queueList[indicator], self.queueList[2*indicator] = self.queueList[2*indicator], self.queueList[indicator]
            indicator = 2 * indicator
        elif(self.queueList[indicator] > self.queueList[2*indicator+1]):
            self.queueList[indicator], self.queueList[2*indicator+1] = self.queueList[2*indicator+1], self.queueList[indicator]
            indicator = 2 * indicator + 1
        else:
            indicator = self.size + 1
        return indicator
class makePath:
    def __init__(self,mazePngFile):
        self.mazeArray = array(Image.open(mazePngFile))
        self.mazeDimensions = [i//2 for i in self.mazeArray.shape[:2]]
    def dijkstra(self,startCell):
        pass

a = priorityQueue()
a.push(3)
a.push(5)
a.push(1)
a.push(1)
a.push(9)
a.push(6)
for i in range(6):
    print(a.get())
