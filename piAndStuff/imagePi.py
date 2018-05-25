import cmath
from math import *
import numpy
from PIL import Image
from random import randint
from piProgram import *


def generateImage(imageSize):
    return piStringToArray(piToStrings(imageSize[0] * imageSize[1] * 3 * 4)[1], imageSize)

def generateImageByDight(imageSize):
    return piStringByDight(piToStrings(imageSize[0] * imageSize[1] * 3 * 4)[1], imageSize)

def piToStrings(givenNumberDights):
    piCalculating = piAlgorithm()
    piValue = piCalculating.calculateDightsPi(givenNumberDights)
    beforeDot,afterDot = generateStringsFromNumber(piValue)
    return beforeDot, afterDot

def generateStringsFromNumber(givenNumber):
    return str(givenNumber).split('.')

def piStringToArray(afterDot, imageSize):
    binaryAfterDot = numpy.binary_repr(int(afterDot))
    listAfterDot = [dight for dight in binaryAfterDot]
    return arrayToImage(listAfterDot[0:imageSize[0] * imageSize[1] * 8 * 3], imageSize)

def piStringByDight(afterDot, imageSize):
    binaryListAfterDot = [numpy.binary_repr(int(dight)) for dight in str(afterDot)]
    stringToArray = ''.join(binaryListAfterDot)
    return arrayToImage([dight for dight in stringToArray][0:imageSize[0] * imageSize[1] * 8 * 3],imageSize)

def arrayToImage(imagelessList, imageSize):
    imagefullArray = numpy.array(imagelessList).reshape(imageSize[0] * imageSize[1] * 3, 8)
    imagefullArray = numpy.array([int(''.join(one),2) for one in imagefullArray.tolist()], numpy.uint8)
    return imagefullArray.reshape(imageSize[0],imageSize[1],3)


if(__name__ == '__main__'):
    imageToGenerate = generateImage((16, 16))
    print(imageToGenerate)
    generatedPiImage = Image.fromarray(imageToGenerate, "RGB")
    generatedPiImage.save("piImage.png")
    generatedPiImage.show()
