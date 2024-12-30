from BuildGraph import BuildGraph
def ShortestPath(edges, src, dest, str):
    graph=BuildGraph(edges)
    print(graph)

    visited = set()
    visited.add(src)
    queue = [[src, 0, str]]

    while queue :
        node, dist, str = queue.pop(0)
        if node == dest:
            return dist, str
   
        for neighbor in graph[node]:
            #print(neighbor, dist)
            if neighbor not in visited:
                visited.add(neighbor) 
                queue.append([neighbor, dist + 1, str + f" ->{neighbor}"])

        
        
    return -1

no_of_edges = int(input("no of edges : "))
edges = [ list(map(int, input(f"edge {i+1} : ").split())) for i in range (no_of_edges) ]

src = int(input("source :"))
dest = int(input("destination :"))

print(ShortestPath(edges, src, dest, f"{src}"))