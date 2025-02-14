
sourceDic = { "S" : [ "B" , "F", "T"],
      "B" : [ "F" ] ,
      "F" : [ "K" ],
      "K" : [ "L" ],
      "L" : [ "C" ],
      "T" : [ "C" ]
      }

queue = list()
visited = set()

def bfs ( visited, graph, root ):
    visited.add(root)
    queue.append(root)

    while queue:
        s = queue.pop(0)
        visited.add(s)
        for n in graph[s]:
            if n not in visited:
                if n in graph:
                    queue.append(n)
            print (  s , "->" , n)

bfs( visited, sourceDic, "S")



