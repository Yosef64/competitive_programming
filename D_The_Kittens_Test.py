n = int(input())
p = [i for i in range(n)]
g = [[i] for i in range(n)]
for i in range(n - 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    x = p[x]
    y = p[y]
    if len(g[x]) < len(g[y]):
        x, y = y, x

    g[x] += g[y]
    for k in g[y]:
        p[k] = x

print(" ".join(map(lambda x: str(x + 1), g[p[0]])))