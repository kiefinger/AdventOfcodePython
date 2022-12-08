import os
import re
import copy

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open("data/day06-1.txt") as file:
    lines = file.readlines()
print (lines)

dl = 4
dl2 = 14

for line in lines:
    line = line.rstrip()

    for i in range( dl-1, len(line) ):
        x = set ( line[i-(dl-1):i+1])
        if  len(x)>= dl :
            print (line, i+1)
            break

    for i in range( dl2-1, len(line) ):
        x = set ( line[i-(dl2-1):i+1])
        if len(x)>= dl2 :
            print (line, i+1)
            break