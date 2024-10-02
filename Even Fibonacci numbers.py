import numpy as np  
import scipy as sp
import matplotlib.pyplot as plt
import random as r
import math as mt

# LINK TO THE PROBLEM https://projecteuler.net/problem=2

# INITIALIZE THE SEQUENCE
FibSeq=np.arange(2)+1
print(FibSeq)

while FibSeq[np.size(FibSeq)-1]<4000000:
    FibSeq=np.append(FibSeq,(FibSeq[np.size(FibSeq)-1]+FibSeq[np.size(FibSeq)-2]))
print(FibSeq)
FibSeq=np.delete(FibSeq,np.size(FibSeq)-1)
print(FibSeq)

# SUM THE EVEN ELEMENTS
result=0
for j in range(np.size(FibSeq)-1):
    if FibSeq[j-1]%2==0:
        result=result+FibSeq[j-1]
print(result)

# Clearly it can be done in many other ways. For example, there is a periodic structure in the sequence: there is one even number every other 2  odd numbers
