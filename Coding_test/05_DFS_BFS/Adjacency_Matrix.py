# Adjacency Matrix

INF = 999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

# print(graph)

# Adjacency List
graph = [[] for i in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)