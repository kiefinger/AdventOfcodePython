import re
import copy
from collections import defaultdict
# Number of vertices
nV = 4
INF = 999

v = {}
e = {}



with open("data/day16-1s.txt") as file:
    lines = file.readlines()
print (lines)
for line in lines:
    line = line.rstrip()
    print (line)
    xy = re.findall(r'Valve (\w+) has flow rate=(\d+); \w+ \w+ to \w+ (.*)',line)
    s,r, t = xy[0]
    t =  t.split(",")
    v[ s] = int(r)
    e[ s] = [ x.strip() for x in t ]
    if int(r) > 0:
        e [s].insert(0,s)


stack = []
openstack = []
#opened = defaultdict( lambda: 0)

maximum = 0
maxdays = 30
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



stack = dsf(stack, 'AA', 1, dict())
print ("Maximum", maximum )