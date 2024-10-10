import numpy as np
import time

#LINK TO THE PROBLEM: https://projecteuler.net/problem=96


def import_grids(file_path):
    grids = []
    current_grid = []

    with open(file_path, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace
            line = line.strip()
            # If the line starts with 'Grid', it's a new grid
            if line.startswith('Grid'):
                # If current_grid has data, save it to grids
                if current_grid:
                    grids.append(current_grid)
                    current_grid = []
            else:
                # Add the 9x9 line to current grid as a list of integers
                if line:
                    current_grid.append([int(char) for char in line])

    # Append the last grid if it exists
    if current_grid:
        grids.append(current_grid)

    return grids

#Read data
file_path = 'Problem 96 data/0096_matrix.txt'  # Change this to the path of your .txt file
grids = import_grids(file_path)
grids=np.array(grids)

#Function that find the allowed moves at position Grid[i,j]=0 
def FindMoves(Grid,i,j):
    Grid[i,j]=0
    MovesRow=np.array([1,2,3,4,5,6,7,8,9])
    MovesColumn=np.array([1,2,3,4,5,6,7,8,9])
    MovesSquare=np.array([1,2,3,4,5,6,7,8,9])
    for k in range(9):
        MovesRow=np.delete(MovesRow,np.argwhere(MovesRow==Grid[i,k]))
        MovesColumn=np.delete(MovesColumn, np.argwhere(MovesColumn==Grid[k,j]))
        MovesSquare=np.delete(MovesSquare, np.argwhere(MovesSquare==Grid[3*(i//3)+k//3,3*(j//3)+k%3]))
    return np.intersect1d(np.intersect1d(MovesRow,MovesColumn),MovesSquare)

#Su Doku solver
def SuDoku_Solver(Grid):
    ResultGrid=Grid.copy()
    ZeroIndices=np.argwhere(ResultGrid==0)
    kIndices=np.zeros(np.size(ZeroIndices)//2,dtype=int)
    r=0
    while r<(np.size(ZeroIndices)//2):
        I=ZeroIndices[r][0]
        J=ZeroIndices[r][1]
        AllowedMoves=FindMoves(ResultGrid,I,J)
        if np.size(AllowedMoves)==0:
            r=r-1
            kIndices[r]=kIndices[r]+1
            continue
        if kIndices[r]==np.size(AllowedMoves):
            kIndices[r]=0
            ResultGrid[I,J]=0
            r=r-1
            kIndices[r]=kIndices[r]+1
            continue
        ResultGrid[I,J]=AllowedMoves[kIndices[r]]
        r=r+1
    return ResultGrid

grids=np.array(grids)



HiddenNumber=[]
for i in range(np.size(grids,0)):
    T1=time.time()
    ResultGrid=SuDoku_Solver(grids[i])
    HiddenNumber.append(int(str(ResultGrid[0,0])+ str(ResultGrid[0,1]) + str(ResultGrid[0,2])))    
    T2=time.time()
    print("Grid ",i+1,"  in time:",T2-T1,"  number:",HiddenNumber[i])

print("Result=",sum(HiddenNumber))
        
        



#This version solves the problem correctly with an iterative precedure. It is quite slow as it uses numpay instead of lists.



