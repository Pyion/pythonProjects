import cmath
from math import *
import numpy
from PIL import Image
from random import randint



def randomImage(imageSize):
    arrayRandom = numpy.zeros(imageSize[0] * imageSize[1] * 3, numpy.uint8)
    for i in range(imageSize[0] * imageSize[1] * 3):
        arrayRandom[i] = randint(0,256)
    return arrayRandom.reshape((imageSize[0], imageSize[1], 3))

if(__name__ == '__main__'):
    imageToGenerate = randomImage((16, 16))
    generatedPiImage = Image.fromarray(imageToGenerate, "RGB")
    generatedPiImage.save("randImage.png")
