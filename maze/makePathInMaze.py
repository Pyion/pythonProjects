import cmath
import numpy
import queue
from PIL import Image
from random import randint,shuffle
from math import *


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
