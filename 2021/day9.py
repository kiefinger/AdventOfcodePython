import os
import re
from collections import defaultdict
from functools import reduce
import operator
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

def inMatrix ( x,y ):
    if x < 0 or x > lenx-1 or y < 0 or y > leny-1:
        return False
    else:
        return True


found = {}
checked = defaultdict(lambda: 0)
#enn jeder nachbar größer ist, dann ist es einer

for y in range(leny):
    for x in range(lenx):
        l = False
        v = matrix[y][x]

        if inMatrix(x,y-1) and matrix[y-1][x] <= v:
            l = True
        if  inMatrix(x,y+1) and matrix[y+1][x] <= v:
            l = True
        if  inMatrix(x-1,y) and matrix[y][x-1] <=v :
            l = True
        if  inMatrix(x+1,y) and matrix[y][x+1] <=v :
            l = True

        if ( not l):
            found[ (x,y)] = v

for x in found.items():
    print (x)
print ( sum( found.values()) + len ( found ) )

# must exclude origin
def neighbours ( x,y  ):
    a=1
    global checked; checked [ (y,x)] = True
    if inMatrix(x,y-1) and matrix[y-1][x] < 9 and not checked[(y-1, x)]: # oben
        a += neighbours( x,y-1)
    if inMatrix(x,y+1) and matrix[y+1][x] < 9 and not checked[(y+1, x)]: #unten
        a += neighbours( x,y+1)
    if inMatrix(x-1,y) and matrix[y][x-1] < 9 and not checked[(y, x-1)]: #links
        a += neighbours( x-1,y)
    if inMatrix(x+1,y) and matrix[y][x+1] < 9 and not checked[(y, x+1)]: #rechts
        a += neighbours( x+1,y)
    return a

area = []
for key,v in found.items():
    print (key)
    (x,y) = key
    print ("berechne :" ,x,y)
    a = neighbours (x, y)
    area.append(a )

# Output: [2, 3, 5, 7, 11]
print ( "All areas" , area)
area.sort()
print ("sort finished")
print ( "All areas" , area)
print ( "Three Areas" , area[0:] )
print ( "Result: ", area[-3:])
rc = reduce(operator.mul,area[-3:])
print ( "Result 2: ", rc)
if rc != 1391940 :
    print ("ERRRO")