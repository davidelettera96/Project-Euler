import time as time
import random as rnd


#LINK TO THE PROBLEM: https://projecteuler.net/problem=426

T0=time.time() #Time controller

#GENERATE INITIAL SEQUENCE:
s0 = int(290797) #initial condition
t=[]
for i in range(2002):
    t.append((s0%64)+1)
    s0 = (s0**2)%50515093
    
#MAKE ENOUGH EMPTY SPACE AT THE END
sum_t = sum(t[i * 2] for i in range(len(t) // 2))
t[-1] = 3 * sum_t
    
    
T1=time.time()
print("Time to generate the initial condition",T1-T0)   #Time control


#GENERATE TEST DATA (SOMETHING THAT CAN BE CHECKED BY HANDS)
t1=[]
for k in range(20):
    t1.append(rnd.randint(1,15))

t1=[2,2,2,1,2,10]

sum_t = sum(t1[i * 2] for i in range(len(t1) // 2))
t1[-1] = 3 * sum_t

    

#---------------FUNCTIONS-------------------------

#UPDATE OF ONE SITE (GROUP OF BALLS)
def move(t,tFixed,i):
    #Point at the next empty space
    j=1
    while t[i+j]==0:
        j=j+2
    
    #Update in the 2 possible cases
    if tFixed[i]<=t[i+j]:
        t[i-1]=t[i-1]+tFixed[i]         #Increase empty space behind
        t[i]=t[i]-tFixed[i]             #Reduce n. of balls
        t[i+j]=t[i+j]-tFixed[i]         #Reduce empty space ahead
        t[i+j-1]=t[i+j-1]+tFixed[i]     #Increase n.balls ahead
        return 
    if tFixed[i]>t[i+j]:
        t[i-1]=t[i-1]+tFixed[i]         #Increase empty space behind
        t[i]=t[i]-tFixed[i]             #Reduce n.balls space behind
        rest=tFixed[i]
        while rest>t[i+j]:
            rest=rest-t[i+j]                #Reduce number of balls still to be moved at next iteration
            t[i+j-1]=t[i+j-1]+t[i+j]        #Increase n.balls ahead
            t[i+j]=0                        #Reduce empty space ahead
            j=j+2
        t[i+j]=t[i+j]-rest          #Last step
        t[i+j-1]=t[i+j-1]+rest      #Last step
        return
    return
        
#UPDATE OF THE ZERO SITE (by def. a separete  function we havoid "if")
def move0(t,tFixed):
    #Point at the next empty space
    j=1
    while t[0+j]==0:
        j=j+2
    
    #Update in the 2 possible cases
    if tFixed[0]<=t[0+j]:
        t[0]=t[0]-tFixed[0]             #Reduce n. of balls
        t[0+j]=t[0+j]-tFixed[0]         #Reduce empty space ahead
        t[0+j-1]=t[0+j-1]+tFixed[0]     #Increase n.balls ahead
        return 
    if tFixed[0]>t[0+j]:
        t[0]=t[0]-tFixed[0]             #Reduce n.balls space behind
        rest=tFixed[0]
        while rest>t[0+j]:
            rest=rest-t[0+j]                #Reduce number of balls still to be moved at next iteration
            t[0+j-1]=t[0+j-1]+t[0+j]        #Increase n.balls ahead
            t[0+j]=0                        #Reduce empty space ahead
            j=j+2
        t[0+j]=t[0+j]-rest          #Last step
        t[0+j-1]=t[0+j-1]+rest      #Last step
        return
    return

#UPDATE THE FULL LIST (call move0() on the first element, move() on the others)
def update(t):
    tFixed=t.copy()
    #Update first site
    move0(t,tFixed)
    #Update all other sites
    L=len(t)
    for i in range(int(L/2)-1):
        move(t,tFixed,2*(i+1))
    #Make enough space at the end for the next update
    sum_t = sum(t[i * 2] for i in range(len(t)//2))
    t[-1] = 3 * sum_t
    return

#EXTRACT THE SIZES OF GROUPS OF BALLS (to check final condition and compute final result)
def check(t):
    L=int(len(t))
    FullList=[]
    for m in range(int(L/2)):
        FullList.append(t[m*2])
    return FullList
    

T3=time.time()
for k in range(1000000):
    print(k)
    Check1=check(t)
    update(t)
    Check2=check(t)
    Check3=Check2.copy()
    Check3.sort()
    if Check1==Check2 and Check2==Check3:
        break
T4=time.time()
print("solved in",k,"updates in time:",T4-T3)

result=0
for n in range(int(len(Check2))):
    result=result+Check2[n]**2
print("final result: ",result)

    
