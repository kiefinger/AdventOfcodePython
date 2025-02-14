import algo.graph
import algo.dijkstra

step = 1
bow  = 1000

DIRS = {
     'W': [ 0,-1 , [  'S' , 'N'  ]],
     'N': [ -1,0 , [  'O' , 'W'  ]],
     'O': [ 0,1  , [  'S' , 'N'  ]],
     'S': [ 1,0  , [  'O' , 'W'  ]]
}

R = [ 'S', 'O', 'N', 'W']

def main() :

    mins = []
    m = []
    start = (0,0)
    ende = (0,0)
    with open("data/day16.txt") as file:
        lines = file.readlines()

    Y=len(lines)
    X=len(lines[0].rstrip())
    g = algo.graph.Graph()

    # two loops, becaose all vertexes must have been created before the edges
    for y in range ( len(lines)):
        line = lines[y].rstrip()
        for x in range ( len(line)):
            c = line[x]
            if (c =='.' or c == 'E'  or c == 'S'):
                for r in R:
                    g.add_vertex( (y,x,r))
                if  c == 'S':
                    start = ( y,x )
                    g.add_vertex( (y,x))
                if  c == 'E':
                    ende = ( y,x )
                    g.add_vertex( (y,x))

    for y in range ( len(lines)):
        line = lines[y].rstrip()
        for x in range ( len(line)):
            c = line[x]
            if (c =='.' or c == 'E'  or c == 'S'):
                for r in R:
                    #print ("Add vertex", y,x,r)
                    ym, xm, dirs  = DIRS[r]
                    for xr in dirs:
                        g.add_edge((y, x, r), (y , x , xr), bow, False)
                        #print("add edge", y, x, r, y , x, xr, bow)
                for r in DIRS:
                    ym, xm, dirs = DIRS[r]
                    if y+ ym >=0 and y+ym < Y and x+xm >= 0 and x+xm < X:
                        if lines[y+ym][x+xm] == '.':
                            g.add_edge((y, x, r ), (y + ym, x +xm, r), 1, True)
                            #print("add edge", y, x, r, y + ym, x + xm, r, 1)
                if  c == 'S':
                    g.add_edge((y, x  ), (y , x, 'O' ), 0, False)
                if  c == 'E':
                    for r in DIRS:
                        g.add_edge((y, x, r ), (y , x ), 0, False)
                        #print("add edge ende", y, x, r, y , x,  0)
#    for v in g:
#        for w in v.get_connections():
#           vid = v.get_id()
#           wid = w.get_id()
#           print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))

    print ( start, ende, g.get_vertex(start) ,g.get_vertex(ende))
    algo.dijkstra.dijkstra(g, g.get_vertex(start), g.get_vertex(ende))

    target = g.get_vertex(ende)
    path = [target.get_id()]
    algo.dijkstra.shortest(target, path)
    print("Path:", path)
    print ( 'The shortest path : %s' %(path[::-1]))
    for p in path:
        xx = g.get_vertex(p)
        print ("Distance", xx,  xx.get_distance())

    print (len(path)-1)
    print ( target.get_distance())



main()
