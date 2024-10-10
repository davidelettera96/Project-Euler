import time

#LINK TO THE PROBLEM: https://projecteuler.net/problem=96

#Import data
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

file_path = 'Problem 96 data/0096_matrix.txt'  # Change this to the path of your .txt file
grids = import_grids(file_path)


#Function that find the allowed moves at position Grid[i,i]=0 
def FindMoves(Grid,i,j):
    Grid[i][j]=0
    Moves=[1,2,3,4,5,6,7,8,9]
    for k in range(9):
        if Grid[i][k] in Moves:
            Moves.remove(Grid[i][k])
        if Grid[k][j] in Moves:
            Moves.remove(Grid[k][j])
        if Grid[3*(i//3)+k//3][3*(j//3)+k%3] in Moves:
            Moves.remove(Grid[3*(i//3)+k//3][3*(j//3)+k%3])
    return Moves

#Su Doku solver
def move(Grid,Zeroes,n):
    if n==len(Zeroes):
        return True
    I=Zeroes[n][0]
    J=Zeroes[n][1]
    AllowedMoves=FindMoves(Grid,I,J)
    for i in AllowedMoves:
        Grid[I][J]=i
        if move(Grid,Zeroes,n+1)==True:
            return True
    Grid[I][J]=0
    return False
        
def Find0(Grid):
    Zeroes=[]
    for i in range(9):
        for j in range(9):
            if Grid[i][j]==0:
                Zeroes.append([i,j])
    return Zeroes
            


#Main
ResultGrids=grids.copy() #Store the results

HiddenNumber=[]
for i in range(0,len(ResultGrids)):#len(grids)):
    T1=time.time()
    Zeroes=Find0(ResultGrids[i])
    move(ResultGrids[i],Zeroes,0)
    HiddenNumber.append(int(str(ResultGrids[i][0][0])+ str(ResultGrids[i][0][1]) + str(ResultGrids[i][0][2])))    
    T2=time.time()
    print("Grid ",i+1,"  in time:",T2-T1,"  number:",HiddenNumber[i])

print("Final Result:",sum(HiddenNumber))

#Solves the problme recursivly, very fast because it is implemented with lists