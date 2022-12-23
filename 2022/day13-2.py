import os
import re
import copy
import algo.graph
import algo.dijkstra
from collections import defaultdict


from collections import defaultdict
import json
import functools
cint = type(0)
carray = type([])

def main() :
    cum = 0
    with open("data/day13-1.txt") as file:

        pas = []
        p =    file.read().split("\n")
        for t in p:
            if len(t) >1:
                pas.append ( json.loads(t) )

        j1 = json.loads("[[2]]")
        j2 = json.loads("[[6]]")
        pas.append( j1 )
        pas.append( j2 )
        pas = sorted( pas, key=functools.cmp_to_key(cmp))

        i1 = pas.index(j1) +1
        i2 = pas.index(j2) +1

        print ("Erg2: ", i1, i2, i2 * i1)


def cmp (left, right):
    for i in range (min(len(left), len(right))):

        if type(left[i]) is cint and type(right[i]) is cint:
            if left[i] < right[i]:
                return -1
            elif left[i] > right[i]:
                return 1
        elif type(left[i]) is carray and type(right[i]) is carray:
            rc = cmp ( left[i], right[i])
            if  rc != 0:
                return rc
        elif type(left[i]) is cint:
            rc = cmp ( [left[i]], right[i])
            if  rc != 0:
                return rc
        elif type(right[i]) is cint:
            rc = cmp ( left[i], [right[i]])
            if  rc != 0:
                return rc
    if len(left) < len(right):
        return -1
    if len(left) > len(right):
        return 1
    return 0

main()
