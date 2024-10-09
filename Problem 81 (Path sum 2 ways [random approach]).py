import numpy as np
import random as rnd

#LINK TO THE PROBLEM: https://projecteuler.net/problem=81

M=np.loadtxt("Problem 82 data/0081_matrix.txt",delimiter=',') 


#Function that takes as imputh the matrix and the path and give the sum
def SumPath(M,path):
    indices=np.where(path==1)
    return np.sum(M[indices])



#Function that evolves the path by one
def MakePath(L):
    path=np.zeros([L,L])
    Start=[0,0]
    path[Start[0],Start[1]]=1
    Move=Start
    while 1==1:
        if Move[0]==L-1:
            path[L-1, Move[1]:]=1
            break
        if Move[1]==L-1:
            path[Move[0]:,L-1]=1
            break
        Coin=rnd.randint(0,1)     #Flip a coin
        if Coin==0:             #Go down
            Move[0]=Move[0]+1
            path[Move[0],Move[1]]=1
        else:                   #Go right
            Move[1]=Move[1]+1
            path[Move[0],Move[1]]=1
    return path
    

#Test on 5x5
TestM=np.array([[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]])

StartSum=SumPath(TestM,MakePath(5))
NewSum=StartSum
for i in range(100):
    temp=SumPath(TestM,MakePath(5))
    if temp<NewSum:
        NewSum=temp
    if i%10==0:
        print(NewSum)
        
#Main on the 80x80 matrix
StartSum=SumPath(M,MakePath(80))
NewSum=StartSum
for i in range(10000000):
    temp=SumPath(M,MakePath(80))
    if temp<NewSum:
        NewSum=temp
    if i%10000==0:
        print(NewSum)
  

    
            
            
            
            
            