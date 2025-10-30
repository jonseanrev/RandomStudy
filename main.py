from RandomSplitMultiple import RSM
from RandomMiddleSquares import RMS
from RandomFourBitMod import Rfbm

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare 


def main():
    # print("First check out Random Split Multiple")
    # rand1 = RSM()
    # print(rand1.seed)
    # rand1a = []
    # rand1b = []
    # for i in range(100):
    #     rand1a.append(rand1.getNext())
    #     rand1b.append(rand1.nextSeed)

    # # print(rand1a)
    # print("random split mult reset:", rand1.resetCount, "times in", i+1,"iterations, with seed", rand1.seed)

    # rand2 = RSM(4321)
    # rand2a = []
    # rand2b = []
    # for i in range(100):
    #     rand2a.append(rand2.getNext())
    #     rand2b.append(str(rand2.nextSeed))

    # # print(rand2a)
    # print("random split mult reset:", rand2.resetCount, "times in", i+1,"iterations, with seed", rand2.seed)


    # print("Next we will check out Random Middle Squares method")
    # rms1 = RMS()
    # rms2 = RMS(10828976372631238)
    # rmsList1 =[]
    # rmsList1a = []
    # for i in range(30):
    #     rmsList1.append(rms1.getNext()) # just gets an int 0-9 from middle of seed but calculates the next seed
    #     rmsList1a.append(int(rms1.nextSeed))
    
    # print("Random Middle Squares seed:", rms1.seed, "reset", rms1.resetCount, "times in ", i+1,"iterations")
    # # print(rmsList1)

    # loopTestValue = 0
    # rmsList2 = []
    # rmsList2a = []
    # sequenceLoop = False
    # j = 0
    # for i in range(100):
    #     rmsList2.append(rms2.getNext()) # just gets an int 0-9 but calculates the next seed 

    #     rmsList2a.append(int(rms2.nextSeed))
    #     if not(sequenceLoop):
    #         if i % 2 == 0 and i > 0:
    #             loopTestValue = rmsList2a[j]
    #             j += 1
    #         if loopTestValue == rmsList2a[i]:
    #             sequenceLoop = True
    #             print(" index:",j, "is a repition of ",i,"value:",loopTestValue)



        
    # print("Random Middle Squares seed:", rms2.seed, "reset", rms2.resetCount, "times in ", i+1,"iterations")
    # bins = np.bincount(rmsList2)
    # chi2_statistic, p_value = chisquare(bins, int(sum(bins)/len(bins)))
    
    # print(bins)
    # print("E: expected")
    # print("O: accutual")
    # print("sum(sqr(O-E)/ E) = chi^2:", chi2_statistic, "p_value:", p_value)
    # print("P_value greater than .05 indicates the value distribution is likely if the sorce is random.")


    fourBitMod = Rfbm()
    fourBitList = fourBitMod.getList(40000)
    fourBitBins = np.bincount(fourBitList)
    print(fourBitBins)
    chi2_statistic, p_value = chisquare(fourBitBins, int(sum(fourBitBins)/len(fourBitBins)))
    print("sum(sqr(O-E)/ E) = chi^2:", chi2_statistic, "p_value:", p_value)

    # print(rmsList2)
    # plt.hist(rmsList2, bins=10, edgecolor='black')
    # plt.plot(rmsList1,rmsList1a , marker='o', linestyle='-', color='red')
    # plt.plot(rmsList2,rmsList2a , marker='o', linestyle='-', color='blue')
    # plt.plot(rmsList2,rmsList2a , marker='o', linestyle='-', color='blue')
    plt.show()


if __name__ == "__main__":
    main()