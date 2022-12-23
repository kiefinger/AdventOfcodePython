import re
import copy
from collections import defaultdict
# Number of vertices
with open("data/day23-1.txt") as file:
    lines = file.readlines()
print (lines)

free = '.'
used = '#'
directions = [ 'N', 'S', 'W', 'O' ]

map = defaultdict(lambda: '.')
mapnext = {}
mapdir = defaultdict(lambda: -1)

def main ():
    global mapnext
    last = None
    for i, line in enumerate(lines):

        line = line.rstrip()
        for e, c in enumerate(line):
            map [ ( e,i) ] = c

    printmap()

    for index in range(10000):
        mapnext = {}
        for x,y in map:
            if  ( x , y ) in  map and map [ ( x , y )] == used:
                neighbours (x,y)
#        print (mapnext)

        countmap = defaultdict(lambda: 0)
        for e in mapnext.values():
            countmap [e] = countmap [e]  + 1

        for step in mapnext:
            to = mapnext[step]
            if countmap[mapnext[step]] <=1:
                move ( step, mapnext[step])

#        printmap()

        if index == 9:
            print ( "Result 1: ", calcFree())

        if  len (mapnext) == 0:
            print ("Resut 2: ", index+1)
            break


def move ( f, t):
    map[ f ] = free
    map[ t ] = used
    mapdir[ t] = mapdir[f]
    del mapdir[f]


def printmap():
    minx = 10000
    maxx = -10000
    miny = 10000
    maxy = -10000
    for x,y in map:
        minx = min( minx, x)
        maxx = max( maxx, x)
        miny = min( miny, y)
        maxy = max( maxy, y)

    for y in range ( miny, maxy+1, 1):
        str = ""
        for x in range ( minx, maxx+1, 1) :
            str += map[(x,y)]
        print (str)

def calcFree():
    minx = 10000
    maxx = -10000
    miny = 10000
    maxy = -10000

    count = 0

    for x,y in map:
        if (x,y) in map and map [ (x,y) ] == used:
            minx = min( minx, x)
            maxx = max( maxx, x)
            miny = min( miny, y)
            maxy = max( maxy, y)

    for y in range ( miny, maxy+1, 1):
        for x in range ( minx, maxx+1, 1):
            if (x,y) not in map or map [ (x,y) ] == free:
                count += 1
    return count

def neighbours(x,y):
    neigh_list = []

    stepsN = [(-1, -1), (0 ,-1),( 1,-1) ]
    stepsS = [(-1,  1), (0 , 1),( 1, 1) ]
    stepsW = [(-1, -1), (-1, 0),(-1 ,1) ]
    stepsO = [( 1, -1), ( 1, 0),( 1, 1) ]
    steps = [ stepsN, stepsS, stepsW, stepsO ]

    dir_index = next_dir(x,y)

    stepsarc = [(0, -1), (0 ,1),( -1,0), ( 1,0 ) ]

    move = False
    for i in range ( 4 ):
        if not checkNeighbours( x,y, steps[(dir_index+i) % 4] ):
            move = True
            break

    if move:
        for i in range ( 4 ):
            if checkNeighbours( x,y, steps[(dir_index+i) % 4] ):
                xx, yy = stepsarc [(dir_index+i) % 4]
                mapnext [ (x,y) ] = (x+xx,y+yy)
                break

def checkNeighbours( x,y, matrix):

    rc = True
    for a,b in matrix:
        if ( x+a , y+b ) in  map and map [ ( x+a , y+b )] == used:
            rc = False
            break
    return rc

def next_dir ( x,y ):

    dir = mapdir [ (x,y)] +1 % 4
    mapdir [ (x,y)] = dir
    return dir;

main()
