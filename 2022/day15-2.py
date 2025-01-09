import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict

from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open("data/day15-1s.txt") as file:
    lines = file.readlines()
print (lines)

sensors = defaultdict(lambda:0)
beacons = {}

minx=100_000_000
maxx=0
miny=100_000_000
maxy=0

def distance ( a, b):
    x,y = a
    x2,y2 = b
    return distance2 (x,y,x2,y2)
def distance2 (x1,y1, x2, y2):
    di = abs(x2-x1) + abs(y2-y1)
    return di


for line in lines:
    line = line.rstrip()
    xy = re.findall(r'.*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+).*',line)
    for i in xy:
        x1,y1,x2,y2 = i
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        sensors[ (x1,y1) ] = (x2,y2)
        beacons [ (x2,y2) ] = (x1,y1)

        print (i)
        minx = min ( minx, x1)
        minx = min( minx, x2)
        maxx = max(maxx,x1)
        maxx = max(maxx,x2)

        miny = min ( miny, y1)
        miny = min( miny, y2)
        maxy = max(maxy,y1)
        maxy = max(maxy,y2)

print ( sensors)

for k  in sensors:
    print ( "Sensor", k , "dist to " , sensors[k] , " = " , distance( k,sensors[k]) )

print ( "MINXX", minx, maxx, miny , maxy)
matrix = []

def printmatrix( matrix ) :
    for i in matrix:
        print (i)

print ("init matrix")
for i in range(miny,maxy,1):
    matrix.append ([ '.' for i in range(minx,maxx,1)])
print ( "init matrix done")

for i in range (miny,maxy,1):
    for e in range(minx,maxx,1):
        for k in sensors:
            x,y = k
            print ( "cmp", i,e,"xy", x,y , "diexy", distance2 ( i,e, x,y ), "dxybb",distance (k, sensors[k]) )
            if distance2 ( i,e, x,y )< distance (k, sensors[k]):
                matrix[i][e] = '#'

printmatrix(matrix)

linemin = 0
linemax = 4_000_000
m2 = defaultdict(lambda:0)
#yyy = 10
yyy = 2_000_000
count = 0
print ( "begin minx =" , minx )
for xxx in range(linemin,linemax+1,1):
    for k in sensors:
        x,y = k
        if not (xxx,yyy) in beacons:
#            print ( "cmp", xxx,yyy,"xy", x,y , "diexy", distance2 ( xxx,yyy, x,y ), "dxybb",distance (k, sensors[k]) )
            if distance2 ( x,y , xxx,yyy ) <= distance (k, sensors[k]):
#                print ( "distance from sensor to ", xxx,yyy, "smaller than distance from sensor ", x,y , "ds", distance2 ( xxx,yyy, x,y ), "dsb",distance (k, sensors[k]) )
                m2[ xxx ] = '#'

print ( "end")

print ( "len", len(m2) )

