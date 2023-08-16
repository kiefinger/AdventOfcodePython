import os
import re
from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open( "data/day9.txt") as file:
    lines = file.readlines()
matrix = []
grid = defaultdict(lambda: 100)

for line in lines:
    print ( line.strip())
    il = [ int(a) for a in list(line.strip())]
    matrix.append(il)
lenx = len( matrix[0])
leny = len( matrix)
print (matrix)

found = {}
#enn jeder nachbar größer ist, dann ist es einer




for y in range(leny):
    for x in range(lenx):
        l = False
#        print ( y,x )
        v = matrix[y][x]
        if ( y> 0 and matrix[y-1][x] <= v):
            l = True
        if ( y< leny-1 and matrix[y+1][x] <= v):
            l = True
        if ( x>0 and matrix[y][x-1] <=v ):
            l = True
        if ( x<lenx-1 and matrix[y][x+1] <=v ):
            l = True
        if ( not l):
            found[ (x,y)] = v

for x in found.items():
    print (x)
print ( sum( found.values()) + len ( found ) )

def neighbours ( x,y ,v  ):
    if ( y> 0 and matrix[y-1][x] <= v):
        l = True
    if ( y< leny-1 and matrix[y+1][x] <= v):
        l = True
    if ( x>0 and matrix[y][x-1] <=v ):
        l = True
    if ( x<lenx-1 and matrix[y][x+1] <=v ):
        l = True
    if ( not l):
        found[ (x,y)] = v

for x in found.items():
    area = neighbours (x.x, x.y, x.value)
    print (x)




