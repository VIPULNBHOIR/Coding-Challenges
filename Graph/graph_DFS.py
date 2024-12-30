def depth(graph,source):
    print(source,end=" -> ")
    for node in graph[source]:
        depth(graph,node)


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

#DFS