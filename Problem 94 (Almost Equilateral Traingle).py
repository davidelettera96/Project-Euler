import time
from math import isqrt



#LINK TO THE PROBLEM: https://projecteuler.net/problem=94
T0=time.time()

MaxPerimeter=1000000000
MaxL=(MaxPerimeter-1)//3

AET=[]
for L in range(2,MaxL):
    Atemp1=(3*L+1)*(L**2-1)*(L+1)
    if isqrt(Atemp1)**2==Atemp1:
        AET.append(3*L+1)
    Atemp2=(3*L-1)*(L**2-1)*(L-1)
    if isqrt(Atemp2)**2==Atemp2:
        AET.append(3*L-1)

T1=time.time()
print("Computed in:",T1-T0)
print("Result:",sum(AET))
        
#I am excluding by hands the degenerate triangle (1,1,2) with area 0  
