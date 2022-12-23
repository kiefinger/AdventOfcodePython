import os
from collections import defaultdict

ds = defaultdict(lambda: 0)
path = []

with open("data/day07-1.txt") as file:
    lines = file.readlines()

for line in lines:
    line= line.rstrip()

    if line.startswith( "dir"):
        pass
    elif line.startswith("$ ls"):
        pass
    elif line.startswith("$ cd .."):
        path.pop()
    elif line.startswith("$ cd"):
        path.append( line[5:] )
    else:
        x = line.split()
        # add size to folder and all parent folder
        for e in range ( len(path)):
            subPath = path[0:e+1]
            ds[ "".join(subPath)  ] += int( x[0])

total = 0
for dir in ds.keys():
    size = ds[dir]
    if size < 100000 :
        total +=size
print ( "Result 1", total)

# calc size of space to be freed
festplatte = 70_000_000
used = ds[ "/"]
free = festplatte - used
necesary = 30_000_000 - free


minFolderSize = 99999999999
for dir in ds.keys():
    size = ds[dir]
    if size< minFolderSize and size >= necesary :
        minFolderSize = size
print ( "min : ", minFolderSize)
#Ergebnis 5974547


