from math import *
from decimal import *

getcontext().prec = 10

class piLebnizSum:
    piValue=1;

    def calculatePiSum(self,numberOfComponents):
        for i in range(1, numberOfComponents+1):
            self.piValue *= (Decimal(4)*Decimal(i)**2)/(Decimal(4)*Decimal(i)**2-Decimal(1))

piSum=piLebnizSum()
piSum.calculatePiSum(8000)
print(piSum.piValue*2)
