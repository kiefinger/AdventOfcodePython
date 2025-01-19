import os
import re
from collections import defaultdict
from functools import reduce
import operator
dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open( "data/day10t.txt") as file:
    lines = file.readlines()
matrix = []
grid = defaultdict(lambda: -1)

dirs = [
    [-1,0],
    [1, 0],
    [0, -1],
    [0, 1],
]
for line in lines:
    il = [ int(a) for a in list(line.strip())]
    matrix.append(il)
lenx = len( matrix[0])
leny = len( matrix)
print (matrix)

def inMatrix ( y,x ):
    if x < 0 or x > lenx-1 or y < 0 or y > leny-1:
        return False
    else:
        return True


checked = defaultdict(lambda: 0)
found = defaultdict(lambda: 0)
null_items = []
#enn jeder nachbar größer ist, dann ist es einer

for y in range(leny):
    for x in range(lenx):
        if ( matrix[y][x] == 0):
            null_items.append( (y,x))

print (null_items)


# must exclude origin
def neighbours ( y,x  ):
    c=matrix[y][x]
    #print ( y,x)
    global checked;
    if matrix[y][x] == 9:
        found[(y, x)] += 1
        checked[ (y,x)] += 1

    for dir in dirs:
        ny = y+dir[0]
        nx = x+dir[1]
        if inMatrix(ny,nx) and checked[ (ny,nx)] !=True and matrix[ny][nx] == c+1:
            neighbours(ny,nx)


for y, x in null_items:
    print(y, x)
    checked = defaultdict(lambda: 0)
    print ( checked)

    neighbours(y,x)

print ( found)
