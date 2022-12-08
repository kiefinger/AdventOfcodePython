import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open("data/day07-1.txt") as file:
    lines = file.readlines()
print (lines)
currentDir = ""
ds = defaultdict(lambda: 0)

path = []
for line in lines:
    line= line.rstrip()

    if line.startswith( "dir"):
        tmp = tmp
    elif line.startswith("$ cd .."):
        currentDir = line[5:]
        path.pop()
    elif line.startswith("$ cd"):
        path.append( line[5:] )
        currentDir = line[5:]
        print ("Path: " , path)
    elif line.startswith("$ ls"):
        tmp = ""
    else:
        print ("Path: " , path, "file", line)
        x = line.split(" ")
        for e in range ( len(path)):
            subPath = path[0:e+1]
            ds[ "".join(subPath)  ] = ds[ "".join(subPath) ] + int( x[0])
        print (ds)

print ( ds )

total = 0
for n in ds.keys():
    s = ds[n]
    if s < 100000 :
        total +=s
print ( "Ergebnis total", total)

ss = [ e for e in ds.values()]
ss.sort()
print (ss)

festplatte = 70_000_000
belegt = ds[ "/"]
frei = festplatte - belegt
benoetigt = 30_000_000 - frei


total = 0
min = 99999999999
for n in ds.keys():
    s = ds[n]
    if s< min and s >= benoetigt :
        min = s
print ( "min : ", min)
#Ergebnis 5974547


