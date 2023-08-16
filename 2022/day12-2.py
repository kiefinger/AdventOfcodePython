import os
import re
import copy
import algo.graph
import algo.dijkstra

from collections import defaultdict
import re
import algo.graph
import algo.dijkstra

# rearange values a=26 z=0 to use dijkstra in the opposite direction
# because dijkstra can be used to find all path from start to all positions, but not vice versa

def main() :

    g = algo.graph.Graph()
    m = []
    start = (0,0)
    ende = (0,0)
    mins = []
    with open("data/day12-1.txt") as file:
        lines = file.readlines()

    for y in range ( len(lines)):
        line = lines[y].rstrip()
        mm = []
        for x in range ( len(line)):
            c = line[x]
            if c == 'S':
                ende = ( x,y )
                mm.append(26)
                g.add_vertex( (x,y))
            elif c == 'E':
                start = (x,y)
                mm.append(1)
                g.add_vertex( (x,y))
            else:
                cc = ord(c)
                if cc >= ord('a') and cc <= ord('z'):
                    mm.append(27-(ord(c)-ord('a')+1))
                    g.add_vertex( (x,y))
        m.append(mm)

#   add edges unidir=false
#   I had to add a feature unidir=false so that add_edge only adds the edge in one direction.
    for y in range ( len(m)):
        for x in range( len(m[y])):
            #R
            if x < len(m[y])-1:
                if m[y][x+1] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x+1,y), 1, False)
            #L
            if x > 0:
                if m[y][x-1] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x-1,y), 1, False)
            #D
            if y < len(m)-1:
                if m[y+1][x] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x,y+1), 1, False)
            #U
            if y> 0:
                if m[y-1][x] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x,y-1), 1, False)

    algo.dijkstra.dijkstra(g, g.get_vertex(start), g.get_vertex(ende))

    for y in range ( len(m)):
        for x in range( len(m[y])):
            if m[y][x] == 26:
                g.get_vertex(ende)
                target = g.get_vertex((x,y))
                path = [target.get_id()]
                algo.dijkstra.shortest(target, path)
                print ( 'The shortest path from ' , start , " to " , (x,y), " : " , path[::-1] )
                if len(path) > 1:
                    print (len(path))
                    mins.append( len(path) -1)

    mins.sort()
    print ( mins)

main()
