
class RMS:
    seedLen = 0
    seed = 0
    nextSeed = 0
    nextRand = 0
    resetCount = 0

    def __init__ (self, newSeed: int = 1234):
        self.seed = newSeed
        self.seedLen = len(str(newSeed))
        self.nextSeed = newSeed
        self.resetCount = 0
        self.getNext()
        
    
    def getNext(self):
        self.nextRand = int(str(self.nextSeed)[int(self.seedLen/2)])

        newNumber = int(self.nextSeed) * int(self.nextSeed)
        
        # reset if we hit 0 
        if newNumber == 0:
            self.nextSeed = self.seed
            self.resetCount += 1
            return self.nextRand

        # if len of n^2 is less than 2*Seed length padd with leading 0's 
        while len(str(newNumber)) < 2*self.seedLen:
            newNumber = '0' + str(newNumber)

        self.nextSeed = self.extractSeed(newNumber, self.seedLen)
        if int(self.nextSeed) == int(self.seed):
            self.resetCount += 1
        return self.nextRand


    @staticmethod
    def extractSeed(num:str, seedLen:int) ->str:
        # seedLen is the length of the seed to be extracted not the given number

        strNum = str(num)
        numLen = len(strNum)
        if seedLen > numLen: 
            return "Error: Seed length longer than source number"
        
        halfSeed = int(seedLen/2)
        halfNum = int(numLen/2)
        startIndex = halfNum - halfSeed

        sMid = strNum[startIndex:startIndex + seedLen]
        
        return sMid

