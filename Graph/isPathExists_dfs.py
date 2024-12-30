from BuildGraph import BuildGraph

def isPathExists(graph, src, dest, visited ):
    
    if src == dest:
        print(src)
        return True

    if src in visited:
        return False
    else:
        print(src," -> ", end='')
    
    visited.add(src)

    for nieghbor in graph[src]:
        if isPathExists(graph, nieghbor, dest, visited):
            return True

    
    return False

"""
no_of_edges = int(input("no of edges : "))
edges = [ list(map(int, input(f"edge {i+1} : ").split())) for i in range (no_of_edges) ]
graph = BuildGraph(edges)
print(graph)

src = int(input("source :"))
dest = int(input("destination :"))
visited = set()
"""
edges = [[0,1],[1,2],[2,0]]
src = 0
dest = 2
visited = set()

graph = BuildGraph(edges)
print(isPathExists(graph, src, dest, visited))
