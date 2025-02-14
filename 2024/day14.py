import os
import re
from collections import defaultdict, Counter, deque, namedtuple
import sympy

re_robot = re.compile(r"p=(?P<x>\d+),(?P<y>\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)")
robotts = []
#X=11
#Y=7
X=101
Y=103
MX=int(X/2)
MY=int(Y/2)
quadrant = [[0,0],[0,0]]


def print_egg(i,e) :
    print ("---------------------------------------------------")
    print (i)
    for i in range (len(e)):
        for u in list(e[i]):
            print ( ' ' if u == 0 else 'X' , end='' )
        print("")
def main():
    p1 = 0
    p2 = 0
    with open( "data/day14.txt" ) as file:
        strMachines = file.read().split('\n')
        for strMachine in strMachines:
            a = re.match(re_robot, strMachine)
            a_robott = { "x": int(a["x"]), "y": int(a["y"]), "vx": int(a["vx"]), "vy": int(a["vy"]) }
            robotts.append (a_robott)

    t = 0
    while t<10000:
        t += 1
        pos = set()
        valid = True

        for r in robotts:
            x = (r["x"]+ t * (r["vx"] + X)) % X
            y = (r["y"] + t * (r["vy"] + Y)) % Y
            if (x, y) in pos:
                valid = False
                break
            pos.add((x, y))

        if valid:
            p2 = t

    for i in range(100):
        isEgg = [ [ 0 for x in range( X) ] for y in range( Y ) ]
        for e in range (len(robotts)):
            r = robotts[e]
            if r["x"] + r["vx"] > 0:
                r["x"]= (r["x"] + r["vx"]) % X
            else:
                r["x"] = (r["x"] + r["vx"] +X ) % X
            if r["y"] + r["vy"] > 0:
                r["y"] = (r["y"] + r["vy"]) % Y
            else:
                r["y"]= (r["y"] + r["vy"] + Y) % Y

#            print (r)
            isEgg[r["y"]][r["x"]] +=1

        #print_egg(i, isEgg)

    for e in range (len(robotts)):
        r = robotts[e]
        if r["x"] != MX and r["y"] != MY :
            #print (r, int((r["x"]-1) / MX), int((r["y"]-1) / MY))
            quadrant[int((r["x"]-1) / MX)][ int((r["y"]-1) / MY)] +=1

    p1 = quadrant[0][0] * quadrant[0][1] * quadrant[1][0] * quadrant[1][1]
    print ( p1, p2)


if __name__ == "__main__":
    main()