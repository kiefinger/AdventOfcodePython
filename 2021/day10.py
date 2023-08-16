import os
import re
from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open( "data/day10-1s.txt") as file:
    lines = file.read().splitlines()

a = { '{' : '}', '[' :']', '(' : ')' , '<' : '>' }
r = { value:key for key,value in a.items() }
openers = [ a for a in a.keys() ]
closers = [ x for x in r.keys() ]

illegal = { ')': 3, "]": 57, '}':1197, '>': 25137 }
stack = []
count = 0
for line in lines:

    print ( line)

    for c in line:
        if c in openers:
            stack.append(c)
        if c in closers:
            if stack[-1] != r[c]:
                count += illegal[c]
                break
            stack.pop()

print ( "Illegal Count" , count )
