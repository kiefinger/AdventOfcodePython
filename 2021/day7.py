
import os
import sys
from collections import defaultdict
from collections import defaultdict
import math

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open( "data/day7.txt") as file:
    data = file.read().split(',')

def gauss ( n ):
    return (n**2+n)/2

distSmMap = defaultdict(lambda: 0)
distSmMap2 = defaultdict(lambda: 0)
data = [int(x) for x in data]
maxItem = max(data)
print ( "Max Item:" , maxItem)
print (data)
print (maxItem)

for i in range(1,maxItem):
    s =0; s2=0
    for e in data:
        dist = abs(e-i)
        s += dist
        s2 += gauss(dist)
    distSmMap[i] = s
    distSmMap2[i] = s2

print (distSmMap)
print (distSmMap2)

min = 99999999999
for d,v in distSmMap.items():
    if v<min:
        min = v;
print ("Solution 1:" , min)

min = 99999999999
for d,v in distSmMap2.items():
    if v<min:
        min = v;

print ("Solution 2:", min)




