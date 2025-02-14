
import graph
import dijkstra

g = graph.Graph()

g.add_vertex((13,1,'N'))
g.add_vertex((12,1,'N'))
g.add_vertex((11,1,'N'))
g.add_vertex((10,1,'N'))
g.add_vertex((10,1,'O'))

g.add_edge((13,1,'N'), (12,1,'N'), 1)
g.add_edge((12,1,'N'), (11,1,'N'), 2)
g.add_edge((11,1,'N'), (10,1,'N'), 3)
g.add_edge((10,1,'N'), (10,1,'O'), 4)

print ('Graph data:')
for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

dijkstra.dijkstra(g, g.get_vertex((13,1,'N')), g.get_vertex((10,2,'W')))

target = g.get_vertex((10,1,'O'))
path = [target.get_id()]
dijkstra.shortest(target, path)
print ( 'The shortest path : %s' %(path[::-1]))