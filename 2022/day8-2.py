import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict

map = []
with open("data/day08-1.txt") as file:
    for line in file.readlines():
        line = line.strip()
        map.append( [ int(i) for i in line ])

leny = len(map)
lenx = len(map[0])
visibleScores = []

def calcDistance (x, a):
    distance = 0
    for i in range (0, len(a)):
        distance += 1
        if a[i] >= x:
            break
    return distance

for y in range (0, leny):
    for x in range(0,lenx):
        left = calcDistance (map[y][x], [map[y][ix] for ix in range (x - 1, -1, -1)])
        right = calcDistance (map[y][x], [map[y][ix] for ix in range (x + 1, lenx)])
        top = calcDistance (map[y][x], [map[iy][x] for iy in range (y - 1, -1, -1)])
        down = calcDistance (map[y][x], [map[iy][x] for iy in range (y + 1, leny)])
        visibleScores.append(max(left, 1) * max(right, 1) * max(top, 1) * max(down, 1))

print ("Result 2: ", max(visibleScores))
#1820 too low
# 1728  far too low
