def IDDFS(graph, start, goal):
    depth = 0

    while True:
        result = DLS(graph, start, goal, depth)

        if result != "not found":
            return result

        depth += 1


def DLS(graph, node, goal, limit):
    if node == goal:
        return [node]

    if limit == 0:
        return "not found"

    for n in graph[node]:
        result = DLS(graph, n, goal, limit - 1)

        if result != "not found":
            return [node] + result

    return "not found"


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print(IDDFS(graph, 'A', 'G'))