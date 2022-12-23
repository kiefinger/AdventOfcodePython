import re
import copy
from collections import defaultdict
# Number of vertices
nV = 4
INF = 999

s = []
pos = {}

class Monkey:
    def __init__(self,val,  prev, next, ):
        self.prev = prev
        self.next = next
        self.val = val

    def __str__(self):
        return str(self.val  )

    def setNext(self, next):
        self.next = next
        self.next.prev = self


with open("data/day20-1.txt") as file:
    lines = file.readlines()
print (lines)

last = None
for i in range ( len(lines)):

    line = lines[i].rstrip()
    val = int(line)
    m = Monkey (val, None, None)
    pos[ i ] = m
    if last != None:
        last.setNext(m)
    last = m
pos[0].prev = last
last.next = pos[0]

lens = len(pos)
def printarray():
    p  = pos[0]
    s = str(p.val) + ", "
    for i in range ( len(pos)-1):
        p = p.next
        s = s +  str(p.val) + ", "

#    print ("array",  s )

printarray()

for i in range ( len(pos)):
    cur = pos [i]
#    print ( "shift ", cur.val)
    if cur.val == 0:
        continue
    if cur.val > 0:
        insert = cur
        for e in range ( cur.val+1):
            insert = insert.next
    else:
        insert = cur
        for e in range ( abs(cur.val)):
            insert = insert.prev

    cur.prev.setNext(cur.next)
    insert.prev.setNext(cur)
    cur.setNext(insert)

    printarray()
nv = []
#find 0
for k in pos:
    if pos[k].val == 0:
        print ("0 is at pos", k)
        e =pos[k]
        for i in range( lens +1):
            nv.append( e.val )
            e = e.next
        break

print ( nv )
print (nv[ 1000 ] , nv[ 2000 ] , nv[ 3000 ] )
print (nv[ 1000 % lens] , nv[ 2000 % lens] , nv[ 3000 % lens] )
sum = nv[ 1000 % lens] + nv[ 2000 % lens] + nv[ 3000 % lens]


print ( sum )
#4136 is too high
#3764 is too high
