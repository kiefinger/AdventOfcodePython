p#
# Aufgabe A
#

import os
import sys
from collections import defaultdict
from collections import defaultdict
import math

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)

with open( "data/day8.txt") as file:
    lines = file.readlines()
i=0

for line in lines:
    parts = line.split('|')
    signals = parts[0].strip().split(" ")
    digits = parts[1].strip().split(" ")

    print ( digits )

    for d in digits:
        if len(d) in {2,3,4,7}:
            i+=1
print ( i)

