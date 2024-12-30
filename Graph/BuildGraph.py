def BuildGraph(edges):
    graph = {}

    for edge in edges:
        node1, node2 = edge
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        
        graph[node1].append(node2)
        graph [node2].append(node1)


    return graph
