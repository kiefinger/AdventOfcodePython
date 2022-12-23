import re
import copy
from collections import defaultdict
# Number of vertices
nV = 4
INF = 999

s = defaultdict(lambda: 0)

maxx = 0
maxy = 0
maxz = 0
minx = 0
miny = 0
minz = 0

with open("data/day19-1.txt") as file:
    lines = file.readlines()
print (lines)



for line in lines:
    line = line.rstrip()
    xyz = line.split(',')
    x,y,z = xyz
    x = int(x); y = int(y); z = int(z)

    s [ (x,y,z) ] = 1
    maxx = max ( maxx, x)
    maxy = max ( maxy, y)
    maxz = max ( maxz, z)
    minx = min ( minx, x)
    miny = min ( miny, y)
    minz = min ( minz, z)


neigbours = [ [ -1, 0, 0], [ 1,0,0 ], [ 0, -1, 0 ], [ 0, 1 , 0 ] , [0,0,-1], [0,0,1] ]

embedded = 0
def check ( x,y,z ) :
    f = 0
    global embedded
    for n in neigbours:
#        print (x,y,z,  "check ",  x+n[0], y+n[1], z+n[2] , "=" ,s [ (x+n[0], y+n[1], z+n[2] ) ])
        if s [ (x+n[0], y+n[1], z+n[2] ) ] == 0:
            f +=1
    return f;

sum = 0

def freeneighbours( x,y, z ):
    free = []
#    print ("chekc n", x,y, z)
    for n in neigbours:
        #        print (x,y,z,  "check ",  x+n[0], y+n[1], z+n[2] , "=" ,s [ (x+n[0], y+n[1], z+n[2] ) ])
        if s [ (x+n[0], y+n[1], z+n[2] ) ] == 0:
            if x+n[0] >= minx and x+n[0] <= maxx and y+n[1] >= miny and y+n[1] <= maxy and z+n[2] >= minz and z+n[2] <= maxz:
                free.append( (x+n[0],y+n[1],z+n[2]))
    return free;

def checkEmbmedded ( x,y, z):
    t = []
    t.append( (x,y, z))
    ch = set()
    while ( len(t)> 0):
        h = t.pop()
        if h not in ch:
            ch.add(h)
            x,y,z = h
            if x <= minx or x >= maxx or y < miny or y >= maxy or z <= minz or z >= maxz:
                return False # muss am rand sein
            f =  freeneighbours (x,y, z)
            for nf in f:
                if nf not in ch:
                    t.append(nf)
        if len (t) > 10000:
            return False

    return True



s2 = s.copy()
for s3 in s2.copy():
  x,y,z = s3
  sum += check ( x,y,z )

print ( sum , embedded)
for x in range ( maxx+1):
    for y in range ( maxy+1 ) :
        for z in range ( maxz+1 ):
            if s[ (x,y,z) ] == 0 and checkEmbmedded(x,y,z):
                anz = check ( x,y, z)
                sum -= (6-anz)
 #               print ( x,y,z , "seems to be partly embeeded ")



print ( sum , embedded)
#4136 is too high
#3764 is too high
