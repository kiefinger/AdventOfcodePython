import os
import re
from collections import defaultdict
from functools import reduce
import operator
matrix = []
found = defaultdict(lambda: 0)
total = 0
dirs = [    [-1,0],    [0, 1],    [1, 0],    [0, -1],]

def main():
    with open( "data/day10t.txt") as file:
        lines = file.readlines()
    for line in lines:
        il = [ int(a) for a in list(line.strip())]
        matrix.append(il)

    for y in range(len( matrix)):
        for x in range(len( matrix[0])):
            if  matrix[y][x] == 0:
                checked = defaultdict(lambda: 0)
                neighbours(y, x, y, x, checked)
    print ( reduce(lambda x, y: x + y, found.values()))

# must exclude origin
def neighbours ( y,x , origy, origx, checked ):
    global total
    c=matrix[y][x]
    if matrix[y][x] == 9:
        found[(origy, origx)] += 1
        #checked[ (y,x)] += 1
        #uncommend checked for part I comment for part II

    for dir in dirs:
        ny = y+dir[0]
        nx = x+dir[1]
        if inMatrix(ny,nx) and checked[ (ny,nx)] !=True and matrix[ny][nx] == (c+1):
            neighbours(ny,nx, origy, origx, checked)

def inMatrix ( y,x ):
    if x < 0 or x > len(matrix[0])-1 or y < 0 or y > len(matrix)-1:
        return False
    else:
        return True

if __name__ == "__main__":
    main()