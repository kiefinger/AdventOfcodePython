import algo.graph
import algo.dijkstra

def main() :

    mins = []
    m = []
    start = (0,0)
    ende = (0,0)
    with open("data/day12-1.txt") as file:
        lines = file.readlines()

    g = algo.graph.Graph()

    for y in range ( len(lines)):
        line = lines[y].rstrip()
        mm = []
        for x in range ( len(line)):
            c = line[x]
            if (c == 'S' ):
                start = ( x,y )
                mm.append(1)
                g.add_vertex( (x,y))
            elif (c == 'E' ):
                ende = (x,y)
                mm.append(26)
                g.add_vertex( (x,y))
            else:
                cc = ord(c)

                if cc >= ord('a') and cc <= ord('z'):
                    mm.append(ord(c)-ord('a')+1)
                    g.add_vertex( (x,y))
        m.append(mm)

    for y in range ( len(m)):
        for x in range( len(m[y])):
            #R
            if ( x< len(m[y])-1):
                if m[y][x+1] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x+1,y), 1, False )
            #L
            if ( x> 0):
                if m[y][x-1] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x-1,y), 1, False )
            #D
            if  y < len(m)-1:
                if m[y+1][x] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x,y+1), 1 , False)
            #U
            if ( y> 0):
                if m[y-1][x] - m[y][x] <= 1:
                    g.add_edge( (x,y), (x,y-1), 1, False )


    algo.dijkstra.dijkstra(g, g.get_vertex(start), g.get_vertex(ende))

    target = g.get_vertex(ende)
    path = [target.get_id()]
    algo.dijkstra.shortest(target, path)
    print ( 'The shortest path : %s' %(path[::-1]))
    print (len(path)-1)



main()
