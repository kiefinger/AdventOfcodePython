import re
import copy
from collections import defaultdict
# Number of vertices
nV = 4
INF = 999

v = {}
e = {}

stack = []
openstack = []
#opened = defaultdict( lambda: 0)

maximum = 0
maxdays = 30
def main():
    global stack

    with open("data/day16-1s.txt") as file:
        lines = file.readlines()
    print (lines)
    for line in lines:
        line = line.rstrip()
        print (line)
        xy = re.findall(r'Valve (\w+) has flow rate=(\d+); \w+ \w+ to \w+ (.*)',line)
        s,r, t = xy[0]
        v[s] = int(r)
        e[s] = [ x.strip() for x in t.split(",") ]
        if int(r) > 0:
            e[s].insert(0,s)

    adj = floyd(initAdj())
    stack = dsf(stack, 'AA', 1, dict())

def initAdj():
    adj = defaultdict(lambda: 0)
    for v1 in v:
        for v2 in v:
            if v1 == v2:
                adj[ ( v1, v2)] = 0
            elif v2 in e[v1]:
                adj[ (v1, v2)] = 1
            else:
                adj[ (v1, v2)] = len(v)+1
    return adj
# Algorithm
def floyd(m):
#    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    # Adding vertices individually
    for r in v:
        for p in v:
            for q in v:
                m[(p,q)] = min(m[(p,q)], m[(p,r)] + m[(r,q)])

    return m
# Printing the output
def sol(dist):
    for p in range(nV):
        for q in range(nV):
            if(dist[p][q] == INF):
                print("INF", end=" ")
            else:
                print(dist[p][q], end="  ")
        print(" ")


def dsf( stack, node, day, opened):
    global maximum
    stack.append(node)

    if day == maxdays:
        sum = 0
        for nkey in opened:
            sum += v[nkey] *  (maxdays-opened[nkey])
        newmaximum = max ( maximum, sum)
        if newmaximum != maximum:
            maximum = newmaximum
            print ("new max = ", maximum, stack, opened)
    elif len(opened) == len(v):
        tmp = copy.deepcopy(opened)
        stack = dsf ( stack, node, day+1, tmp )
    else :
        edges = e[node]
        for edge in edges:
            if edge == node:
                if not edge in opened and v[edge] > 0:
                    tmp = copy.deepcopy(opened)
                    tmp [ edge] = day
                    stack = dsf ( stack, edge, day+1, tmp)
            else:
                if len(stack)>3 and edge == stack[-2] and node == stack[-3]:
                    tmp = 1
                else:
                    tmp = copy.deepcopy(opened)
                    stack = dsf ( stack, edge, day+1, tmp)
    stack.pop()
    return stack




main()