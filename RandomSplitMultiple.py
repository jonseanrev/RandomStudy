
from typing import Tuple

class RSM():
    seedLen = 0
    seed = 0
    nextSeed = 0
    nextRand = 0
    resetCount = 0
    
    def __init__(self, num: int = 12330654311213):
        self.resetCount = 0
        self.seed = num
        self.nextSeed = num
        self.seedLen = len(str(num))
        
        self.getNext() 
         
    def getNext(self) -> int:

        # first just grab middle int from nextSeed
        half = int(self.seedLen/2)
        nsStr = str(self.nextSeed)
        self.nextRand = int(nsStr[half])

        # recalc nextSeed 
        newSeed = RSM.calNextFromInt(self.nextSeed)
        # if we hit zero we revert back to the starting seed
        if newSeed == 0: 
            self.nextSeed = self.seed 
            self.resetCount += 1
        else:
            self.nextSeed = newSeed

        return self.nextRand 


    @staticmethod
    def calNextFromInt(num: int) -> int:
        nums = RSM.splitInt(num)
        new = nums[0] * nums[1]
        string1 = str(num)
        string2 = str(new)
        while len(string2)<len(string1):
            # print(string2)
            string2 += "0"
        
        return int(string2)

    @staticmethod
    def splitInt(num: int) -> Tuple[int,int]:
        sNum = str(num)
        length = len(sNum)
        half = int(length/2)
        num1 = int(sNum[0:half])
        num2 = int(sNum[half:length])
        return [num1,num2]
        