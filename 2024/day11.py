import os
import re
from collections import defaultdict, deque
from functools import reduce
import operator
found = defaultdict(lambda: 0)



def main():
    with open( "data/day11.txt") as file:
        line = file.readline()
        stones =   list(line.split())
        for stone in stones:
            found[stone] += 1
        for i in range(75):
            old = found.copy()
            for f in list(old):
                if old[f]>0:
                    r = blink(f)
                    found [f] -= old[f]
                    found [r[0]] += old[f]
                    if len(r) == 2:
                        found [r[1]] +=old[f]
        total = 0
        for h in found:
            total += found[h]
        print (total)

def blink ( stone ):
    if  int(stone) ==0:
        return ["1"]
    elif (len(stone)%2)==0:
        l = len(stone)
        a = stone[0:int(l/2)]
        b = stone[int(l/2):]
        b = str(int(b))
        return [a,b]
    else:
        return [str(int(stone)*2024)]
if __name__ == "__main__":
    main()