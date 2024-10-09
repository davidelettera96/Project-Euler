import numpy as np

#LINK TO THE PROBLEM: https://projecteuler.net/problem=82

Mstart=np.loadtxt("Problem 81 data/0081_matrix.txt",delimiter=',') 
M=np.loadtxt("Problem 81 data/0081_matrix.txt",delimiter=',') 

L=int(np.sqrt(np.size(M)))

#Compute the cost of going to a site in the column j starting somewher in (j-1)
def MoveRight(j,M):
    M_new=np.copy(M)
    for i in range(L):
        MinPath=np.max(M)
        for k in range(L):
            if k<i:
                temp=np.sum(M[:,j][k:i])+M[k][j-1]
                PathCost=min(M[i,j-1],temp)
            if k>i:
                temp=np.sum(M[:,j][i+1:(k+1)])+M[k][j-1]
                PathCost=min(M[i,j-1],temp)
            if i==k:
                PathCost=M[i,j-1]
            MinPath=min(MinPath,PathCost)  
        M_new[i][j]=M_new[i][j]+MinPath
    return M_new
        
                
UpdatedM=M
for n in range(1,L):
    UpdatedM=MoveRight(n,UpdatedM)

print("The solution is",np.min(UpdatedM[:,L-1]))

     