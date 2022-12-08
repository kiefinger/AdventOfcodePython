import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open("data/day09-1s.txt") as file:
    lines = file.readlines()
print (lines)

leny = len(lines)
lenx = len(lines[0].rstrip())

for line in lines:
    line = line.rstrip()



print ("Result 2: ", 1)
print ("Result 1: ", 1)
