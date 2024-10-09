import numpy as np
import time

#LINK TO THE PROBLEM: https://projecteuler.net/problem=81
T0=time.time()

M=np.loadtxt("Problem 81 data/0081_matrix.txt",delimiter=',') 

L=int(np.sqrt(np.size(M)))

temp=0
for i in range(L):
    for j in range(L):
        if i!=0 and j!=0:
            temp=min(M[i-1][j],M[i][j-1])
            M[i][j]=M[i][j]+temp
        if i!=0 and j==0:
            temp=M[i-1][j]
            M[i][j]=M[i][j]+temp
        if j!=0 and i==0:
            temp=M[i][j-1]
            M[i][j]=M[i][j]+temp

T1=time.time()
print("The result is:",int(M[L-1,L-1]),"(solved in",T1-T0,")")
            