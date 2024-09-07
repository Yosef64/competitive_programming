def find_initial_arrangement(n, pairs):
    """
    Find any possible initial arrangement of the kittens into n cells.

    Args:
        n (int): The number of kittens.
        pairs (list): A list of pairs of kittens that want to play together.

    Returns:
        list: A list of indices of kittens, where the i-th element is the index of the kitten originally in the i-th cell.
    """
    # Build the graph
    graph = [[] for _ in range(n + 1)]
    for x, y in pairs:
        graph[x].append(y)
        graph[y].append(x)

    # Find a Hamiltonian path in the graph
    def find_hamiltonian_path(graph):
        def dfs(node, path):
            if len(path) == n:
                return path
            for neighbor in graph[node]:
                if neighbor not in path:
                    new_path = dfs(neighbor, path + [neighbor])
                    if new_path:
                        return new_path
            return None

        for i in range(1, n + 1):
            path = dfs(i, [i])
            if path:
                return path

    # Find a Hamiltonian path in the graph
    path = find_hamiltonian_path(graph)

    return path

# Read input
n = int(input())
pairs = []
for _ in range(n - 1):
    x, y = map(int, input().split())
    pairs.append((x, y))

# Call the function and print the result
result = find_initial_arrangement(n, pairs)
for i in result:
    print(i)