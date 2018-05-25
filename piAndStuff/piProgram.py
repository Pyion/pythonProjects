from math import *
from decimal import *

globalNumberDights = 1000

class piAlgorithm:
    aRecurention = Decimal((2)).sqrt()
    bRecurention = Decimal(0)
    pRecurention = Decimal(2+Decimal(2).sqrt())
    numberOfRecurention = Decimal(0)

    def increaseNumberOfRecurention(self):
        aRecurentionUpdate = ((self.aRecurention).sqrt() + Decimal(1)/(self.aRecurention.sqrt())) / Decimal(2)
        bRecurentionUpdate = ((Decimal(1) + self.bRecurention) * (self.aRecurention).sqrt()) / (self.aRecurention + self.bRecurention)
        pRecurentionUpdate = ((Decimal(1) + aRecurentionUpdate) * self.pRecurention * bRecurentionUpdate) / (Decimal(1) + bRecurentionUpdate)
        self.aRecurention = aRecurentionUpdate
        self.bRecurention = bRecurentionUpdate
        self.pRecurention = pRecurentionUpdate
        self.numberOfRecurention += Decimal(1)
        return(self.pRecurention)

    def calculateDightsPi(self,howManyDights=1000):
        getcontext().prec = howManyDights
        oldPiWalue = Decimal(0)
        while(oldPiWalue != self.pRecurention):
            oldPiWalue = self.pRecurention
            self.increaseNumberOfRecurention()
        return self.returnPi()

    def returnPi(self):
        return (self.pRecurention)

if(__name__=="__main__"):
    piCalculating = piAlgorithm()
    piFile=open('pi','w')
    piFile.write(str(piCalculating.calculateDightsPi(globalNumberDights)))
    piFile.close()
    print(piCalculating.numberOfRecurention)
