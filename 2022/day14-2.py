import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict

from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open("data/day14-1.txt") as file:
    lines = file.readlines()
print (lines)

map = []

for line in lines:
    line = line.rstrip()
    paths = line.split("->")
    paths = [ path.split(",") for path in paths]
    paths = [ ((int(path[0]), int(path[1]))) for path in paths]
    map.append(paths)

minx=1000
maxx=0
miny=1000
maxy=0

def printMatrix(matrix):
    print ("Matrix")
    for i in matrix:
        print ( i[minx:maxx])

for i in map:
    for e in i:
        x,y  = e
        minx = min (minx,x)
        maxx = max(maxx,x)
        maxy = max(maxy,y)


print ( minx,maxx, miny, maxy)


xd = minx
xl = maxx - minx
bottom = maxy +2

print ("matixlen", xl, maxy)
matrix = defaultdict(lambda:0)
#for i in range ( maxy+2 ):
#    matrix.append ( [ 0 for e in range ( maxx+2 )])

#bottomline
for i in range(-1000,1000,1):
    matrix [(bottom,i)] = 1

for path in map:
    print ( "path", path)
    start = path[0]
    for w in path[1:]:
        x,y = start
        xx,yy = w
        print ("line from ", start, w)
        if x==xx:
            for yi in range ( min(y,yy), max(y,yy)+1):
                print ( "x", x, yi)
                matrix[(yi,x)] = 1
        if y==yy:
            for xi in range ( min(x,xx), max(x,xx)+1):
                print ( "y2", y,xi)
                matrix[(y,xi)] = 1
        start = w




sandstart = (500,0)

def movesand ( matrix, sand):
    blocked = False
    outofBounds = False
    x,y = sand


#    print ("movesand", x,y )

    if matrix[(y+1,x)] == 0:
        sand = (x,y+1)
    elif matrix[(y+1,x-1)] == 0:
        sand = (x-1,y+1)
    elif matrix[(y+1,x+1)] == 0:
        sand = (x+1,y+1)
    else:
        # blocked
        print ("block", x,y)
        matrix [(y,x)] = 2
        blocked = True

    if sand == (500,0):
        outofBounds = True

    return sand, outofBounds, blocked

nsands = 0
while True:
    outofBound = False
    sand = sandstart
    nsands +=1
    blocked = False
    while blocked == False:
        sand, outofBound, blocked=  movesand ( matrix, sand)
#        printMatrix(matrix)
        if outofBound:
            break
        if blocked:
            break
    if outofBound:
        break

print ("Result 2: ", 1)
print ("Result 1: ", nsands-1)
#25499 too low