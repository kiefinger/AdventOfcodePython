import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open("data/day08-1.txt") as file:
    lines = file.readlines()
print (lines)
currentDir = ""

leny = len(lines)
lenx = len(lines[0].rstrip())

outside = 2*leny + 2*lenx-4
print ("Outsde", leny, lenx , outside)

map = []
for line in lines:
    line = line.strip()
    map.append( [ int(i) for i in line ])

print (map)

def checkpoint (x,y):
    left = True
    for xx in range (0,x):
        if map[y][xx] >=map[y][x]:
            left = False
    right = True
    for xx in range (x+1, lenx):
        if map[y][xx] >=map[y][x]:
            right = False
    top = True
    for yy in range (0,y):
        if map[yy][x] >=map[y][x]:
            top = False
    down = True
    for yy in range (y+1, leny):
        if map[yy][x] >=map[y][x]:
            down = False
    return left or right or top or down

count =0
for y in range (1, leny-1):
    for x in range(1,lenx-1):
        if checkpoint(x,y):
            count += 1

print ( "Result 1:" , count + outside)


def checkline (x, a):
    distance = 0
    for i in range (0, len(a)):
        distance += 1
        if a[i] >= x:
            break
    return distance

vis = []

for y in range (0, leny):
    for x in range(0,lenx):

        l = [ map[y][xx] for xx in range (x-1,-1,-1) ]
        r = [ map[y][xx] for xx in range (x+1, lenx) ]
        t = [ map[yy][x] for yy in range ( y-1, -1, -1) ]
        d = [ map[yy][x] for yy in range (y+1, leny) ]

        left = checkline ( map[y][x], l)
        right = checkline ( map[y][x], r)
        top = checkline ( map[y][x], t)
        down = checkline ( map[y][x], d)
        vis.append(max(left,1) * max(right,1) * max(top,1) * max(down,1))

print ("Result 2: ", max(vis))
#1820 too low
# 1728  far too low
