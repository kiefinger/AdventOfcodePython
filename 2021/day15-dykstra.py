
import os
import re
import algo.graph
import algo.dijkstra
from queue import PriorityQueue

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)
with open( "data/day15s.txt") as file:
    lines = file.readlines()

print ( lines )

lenx = len(lines[0].rstrip())
leny = len(lines)

g = algo.graph.Graph()

v = {lenx * leny}

for y in range(leny):
    for x in range (lenx):
        g.add_vertex( (x,y))


for y in range(leny):
    line = lines[y]
    line = line.rstrip()
    if y < leny-1:
        nextline = lines[y+1]
    for x in range (lenx):
        if x < lenx-1:
            print ( "edge (" , x,y, ") -> (", x+1, y , ")" )
            g.add_edge ( (x,y), ( x+1, y) , int(line[x+1]))
        if y < leny-1:
            print ( "edge (" , x,y, ") -> (", x, y+1 , ")" )
            g.add_edge ( (x,y), ( x, y+1) , int(nextline[x]))

#    g.add_edge(0, 1, 4)

algo.dijkstra.dijkstra(g, g.get_vertex((0,0)), g.get_vertex((9,9)))

target = g.get_vertex((9,9))
path = [target.get_id()]
algo.dijkstra.shortest(target, path)
print ( 'The shortest path : %s' %(path[::-1]))



distance = 0
path.reverse()
for p in path:
    x,y = p
    distance += int(lines[y][x])
    print( "Calc diff", p,lines[y][x] )

print ("Ergebnis", distance)

distance2 = algo.dijkstra.shortest_path_distance(target, 0)
print ("Ergebnis", distance2)