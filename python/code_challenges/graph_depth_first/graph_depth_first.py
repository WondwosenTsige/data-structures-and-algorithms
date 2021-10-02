def dfs(graph, vertex):
    visited = []
    for neighbour in graph.neighbours (vertex):
        if not visited(neighbour):
            visited.append(neighbour)
        dfs(graph,neighbour)
