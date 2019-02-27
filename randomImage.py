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

def extendImage(imageArray,dim):
    newImageArray = numpy.zeros(len(imageArray)*len(imageArray[0])*3*dim*dim, numpy.uint8).reshape((dim*len(imageArray),dim*len(imageArray),3))
    for i in range(len(imageArray)):
        for j in range(len(imageArray[i])):
            for k in range(dim):
                for l in range(dim):
                    newImageArray[i*dim+k][j*dim+l] = imageArray[i][j]
                    #print(i,j,newImageArray[i*dim+k][j*dim+l],imageArray[i][j])
    print(newImageArray)
    return newImageArray


if(__name__ == '__main__'):
    imageToGenerate=randomImage((16, 16))
    imageToGenerateExtended = extendImage(imageToGenerate,64)
    generatedPiImage = Image.fromarray(imageToGenerate, "RGB")
    generatedPiImage.save("randImage.png")
    generatedPiImage = Image.fromarray(imageToGenerateExtended, "RGB")
    generatedPiImage.save("randImage2.png")
