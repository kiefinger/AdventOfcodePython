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
map = []
count =0
leny = len(lines)
lenx = len(lines[0].rstrip())
outside = 2*leny + 2*lenx-4

for line in lines:
    line = line.strip()
    map.append( [ int(i) for i in line ])

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

for y in range (1, leny-1):
    for x in range(1,lenx-1):
        if checkpoint(x,y):
            count += 1

print ( "Result 1:" , count + outside)
#1870