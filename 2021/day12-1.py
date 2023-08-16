
import os
import re
import algo.graph
import algo.dijkstra

dir_path = os.path.dirname ( os.path.realpath(__file__))
print (dir_path)
with open( "data/day12-1s.txt") as file:
    lines = file.readlines()

g = algo.graph.Graph()

for line in lines:
    a,b = line.strip().split("-")
    print  (a,b)
    if g.get_vertex(a) is None:
        g.add_vertex(a)
    if g.get_vertex(b) is None:
        g.add_vertex(b)
    g.add_edge(a,b)


for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

#algo.dijkstra.dijkstra(g, g.get_vertex('a'), g.get_vertex('e'))

#target = g.get_vertex('e')
#path = [target.get_id()]
#algo.dijkstra.shortest(target, path)
#print ( 'The shortest path : %s' %(path[::-1]))

# breitensuche
queue = []
visited = set()

def bfs ( visited , graph, root ):
    graph.get_vertex(root).set_visited()
    queue.append(graph.get_vertex(root))

    while queue:
        s = queue.pop(0)
        s.set_visited()
        for n in s.adjacent:
            if not n.visited:
                queue.append(n)
            print (  s , "->" , n)

def dfs ( visited , graph, root , path, paths):

    s = graph.get_vertex(root)
    print ( "Visiting node:" , path, s.id)
    path.append(s.id)
    if s.id == "end" :
        paths.append(path[:])
    else:
        for n in s.adjacent:
            if s.id == "b" and n.id == "end":
                print (  s , "->" , n)
            if ( not (n.id in path) ) or  ( n.id in path and n.id.isupper() ):
                paths, path = dfs ( visited, graph, n.id, path, paths)

    path.pop()
    return paths, path

paths = []
path= []
paths, path = dfs( visited, g, "start", path,  paths)
print (paths)
print (len(paths))
