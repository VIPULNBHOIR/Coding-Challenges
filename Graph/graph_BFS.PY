def depth(graph,source):

    queue=[source]

    while len(queue) > 0:
        element=queue.pop(0)
        print(element,end=' - > ')
        
        for node in graph[element]:
            queue.append(node)


gragh={
    'a':['b','c','h'],
    'b':['d'],
    'c':['e'],
    'd':[],
    'e':[],
    'h':['k'],
    'k':[]
}

depth(gragh,'a')

#BFS