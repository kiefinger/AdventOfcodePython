import os
import re
from collections import defaultdict

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)
with open( "data/day5.txt") as file:
    lines = file.readlines()

overlap = defaultdict(lambda: 0)

def addLine ( x1, y1, x2, y2):
    dx = 1 if x2>=x1 else -1
    dy = 1 if y2>=y2 else -1
    if y1 == y2:
        for x in range(x1,x2+1*dx, dx ):
            overlap[ (y1, x)] +=1
    elif x1 == x2:
        for y in range(y1,y2+1*dy, dy):
            overlap[ (y, x1)] +=1
    else:
        # the distance between x1-x2 must be the same as y1-y2. otherwise not 45
        # unclear if ths is the case, or if lines that are not 45 ° must be dismissed.
        # test seems ok. not exceptions.
        # ddx = x2-x1 if x2>x1 else x1-x2
        # ddy = y2-y1 if y2>y1 else y1-y2

        ydd=0
        for x in range(x1,x2+1*dx, dx ):
            overlap[ (y1 + ydd * dy, x)] +=1
            ydd+=1

for line in lines:
    line = re.sub(" -> ",",", line)
    numbers = [int(c) for c in line.strip().split(",")]
    addLine( numbers[0], numbers[1], numbers[2], numbers[3])

count = 0

for v in overlap.values() :
    if v>1:
        count +=1

print ( count )

