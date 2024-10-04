import numpy as np  
from functools import lru_cache 


#LINK TO THE PROBLEM:   https://projecteuler.net/problem=286

q=50.001 #(starting point)


@lru_cache(maxsize=None) #This is CRUCIAL, without it is way too slow
def probability(q,m,d): #probability to have made exactly m shots at distance d
    if m==d:
        return np.prod(1-(np.arange(1,d+1))/q)
    if m==0:
        return np.prod((np.arange(1,d+1))/q)
        
    result=(1-d/q)*probability(q,m-1,d-1)+(d/q)*probability(q,m,d-1)
    return result

test=probability(q,20,50)
print(test)

#Search the result by bisection
qTarget=q
Dq=1
while Dq>10**(-11):
    n=0
    while (probability(qTarget+n*Dq,20,50)-0.02)*(probability(qTarget+(n+1)*Dq,20,50)-0.02)>0:
        n=n+1
    qTarget=qTarget+n*Dq
    Dq=Dq/10

print("The terget value of q is:",qTarget)