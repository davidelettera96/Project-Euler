import time as time


#LINK TO THE PROBLEM: https://projecteuler.net/problem=426

T0=time.time() #Time controller

#GENERATE INITIAL SEQUENCE:
s0 = int(290797) #initial condition
t=[]
for i in range(1000):
    t.append((s0%64)+1)
    s0 = (s0**2)%50515093
    
#MAKE ENOUGH EMPTY SPACE AT THE END
sum_t = sum(t[i * 2] for i in range(len(t) // 2))
t[-1] = 3 * sum_t
    
T1=time.time()
print("Time to generate the initial condition",T1-T0)   #Time control



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

#Check if the first part of the list is already ordered. Give output i such that from 0 to i the list does not need to be updated anymore
def remember(t,i_start):
    i=i_start
    L=len(t)
    while t[i]<=t[i+1]: #and t[i+2]-t[i]>=0:
        if i==L-2:
            break
        i=i+2
    return i

#UPDATE THE FULL LIST (call move0() on the first element, move() on the others)
def update(t,i_start):
    tFixed=t.copy()
    #Update first site
    if i_start==0:
        move0(t,tFixed)
    #Update all other sites
    L=len(t)
    for i in range(max(i_start,2),L,2):
        move(t,tFixed,i)
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
i_start=0
#print("starting t",t)
for k in range(1000000):
    i_start=remember(t,i_start)
    print("i_start",i_start)
    #print("t",t)
    Check1=check(t)
    update(t,i_start)
    Check2=check(t)
    if Check1==Check2:  #Not trivial that this condition is enough
        break
T4=time.time()
print("i_start",i_start)
print("solved in",k,"updates in time:",T4-T3)
#print("final t",t)

result=0
for n in range(int(len(Check2))):
    result=result+Check2[n]**2
print("final result: ",result)

#PUSHED TO 100000 WITH RESULT:
    #solved in 64383 updates in time: 375.15719413757324
    #final result:  354376745
    
