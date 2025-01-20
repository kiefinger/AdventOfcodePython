import os
import re
from collections import defaultdict
from functools import reduce
import operator


matrix = []
grid = defaultdict(lambda: -1)
checked = defaultdict(lambda: 0)
found = defaultdict(lambda: 0)
null_items = []
total = 0

dirs = [
    [-1,0],
    [0, 1],
    [1, 0],
    [0, -1],
]

def inMatrix ( y,x ):
    if x < 0 or x > len(matrix[0])-1 or y < 0 or y > len(matrix)-1:
        return False
    else:
        return True

# must exclude origin
def neighbours ( y,x , origy, origx, checked ):
    global total
    c=matrix[y][x]
    #print ( "in", y,x, c)
    if matrix[y][x] == 9:
        found[(origy, origx)] += 1
        checked[ (y,x)] += 1
        #print ( found )

    for dir in dirs:
        ny = y+dir[0]
        nx = x+dir[1]
        #print ( ny, nx, checked[ (ny,nx)])
        if inMatrix(ny,nx) and checked[ (ny,nx)] !=True and matrix[ny][nx] == (c+1):
            neighbours(ny,nx, origy, origx, checked)

def main():
    with open( "data/day10t.txt") as file:
        lines = file.readlines()
    for line in lines:
        il = [ int(a) for a in list(line.strip())]
        matrix.append(il)
    lenx = len( matrix[0])
    leny = len( matrix)
    print (matrix)


    #enn jeder nachbar größer ist, dann ist es einer

    for y in range(leny):
        for x in range(lenx):
            if ( matrix[y][x] == 0):
                null_items.append( (y,x))

    print (len(null_items), null_items)

    for y, x in null_items:
        print(y, x)
        checked = defaultdict(lambda: 0)
        neighbours(y,x,y,x, checked)
        print ( "found" , found, len(checked), checked)

    total = 0
    for b in null_items:
        total += b

if __name__ == "__main__":
    main()