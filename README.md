This is a basic study of psudeo random generation. 

RandomSplitMultiple shows how quickly a poor algorithms squence collapses into a loop. 

RSM: n is a number such that n_f is the first half of the digits of n and n_s is the second half. 
n1 = n_f * n_s, n2 = n1_f * n1_s, and so on.   

RandomMiddleSquares is better but it collapses in fewer itterations than it's seed length. 

RMS: n is a number such that n1 is the center digits of n^2 or n1 = C(n^2) where the function C extracts the order of n digits from n^2. if n = 12, n^2 = 144, n1 = C(144) = 14, n2 = C(n1) and so on. 

Chi^2 analysis on smaller sets of RMS with a largenough seed pass random test. That is, if RMS doesn't fall into a loop, it is difficult to determin that it is not random by it's output alone.    