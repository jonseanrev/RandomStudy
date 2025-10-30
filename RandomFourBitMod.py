

class Rfbm:

    # these are all being treated as static 
    bits = 4
    seedLen = 0
    seed = 0
    fbSet = []
    staticIndex = 0

    def __init__(self, seed = 12345):
        Rfbm.seed = seed
        Rfbm.seedLen = len(str(seed))

        self.reSetFbset()
        

    def getList(self, size: int):
        l = []
        for i in range(size):
            l.append(self.getNextInt())
        return l

    def getNextInt(self) -> int:
        binaryStr = self.getBitSet(3)
        decStr = str(self.byteToDec(binaryStr))
        return int(decStr[len(decStr)-1])


    def getBitSet(self, size: int) -> str:
        l = ''
        for i in range(size):
            byte = self.getNextByte()
            l += byte
        return l 


    @staticmethod
    def getNextByte() -> str:
        listLen = len(Rfbm.fbSet)
        if len(Rfbm.fbSet) < 1:
            Rfbm.reSetFbset()
            listLen = len(Rfbm.fbSet)
        index = (Rfbm.seed + Rfbm.staticIndex) % listLen

        Rfbm.staticIndex += 1
        
        return Rfbm.fbSet.pop(index)

    @staticmethod
    def padBinary(bNum:str,bitLength:int) -> str:

        if len(bNum) > bitLength:
            return "Error Input binary is longer than requested bit Length."
        
        while len(bNum) < bitLength:
            bNum = '0' + bNum 
        
        return bNum

    @staticmethod
    def cleanBin(decimalNum:int)->str:
        return bin(decimalNum)[2:]

    @staticmethod
    def reSetFbset():
        Rfbm.fbSet = []
        for i in range(Rfbm.bits * Rfbm.bits):
            Rfbm.fbSet.append(Rfbm.padBinary(Rfbm.cleanBin(i), Rfbm.bits))
    @staticmethod
    def byteToDec(byte:str) -> int:
        return int(byte, 2)
    
