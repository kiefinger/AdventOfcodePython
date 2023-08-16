import os
import re
import copy
import algo.graph
import algo.dijkstra
from collections import defaultdict


from collections import defaultdict
import json
ds = defaultdict(lambda: 0)
cint = type(0)
carray = type([])

def main() :
    cum = 0
    with open("data/day13-1.txt") as file:
        #lines = file.readlines()

        pas = []
        p =    file.read().split("\n\n")
        for t in p:
            pas.append ( [ x for x in t.split ( "\n")])

        index = 1
        for s in pas:
            left = json.loads(s[0])
            right = json.loads(s[1])
            print ( left, right)

            rc = cmp( left, right)
            if  rc <0 :
                print ( "pair" , index ,", in right order")
                cum += index
            index += 1

        print ("Erg1: ", cum)


def cmp (left, right):
    print ( "compare" , left, right)
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
