def count_trees(n, p):
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        graph[i + 1].append(p[i])
        graph[p[i]].append(i + 1)

    visited = [False] * (n + 1)

    tree_count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            tree_count += 1
            dfs(graph, visited, i)

    return tree_count

def dfs(graph, visited, vertex):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

n = int(input())
p = list(map(int, input().split()))
print(count_trees(n, p))