from collections import defaultdict


n , m = map(int,input().split())
graph = defaultdict(set)
for _ in range(m):
    v , u = map(int,input().split())
    graph[v].add(u)
    graph[u].add(v)
ans , v = 0 , set()
# print(graph)
def dfs(cur,path):
    # nonlocal ans 
    print(graph[cur],path)
    if cur in path:
        print("yes")
        ans += 1
        
    if cur in v:
        return 
    v.add(cur)
    for child in graph[cur]:
        if child not in v:
            dfs(child,path.union({cur}))
    return 

for node in range(1,n+1):
    if node not in v:
        dfs(node,set())
print(ans)
    
            
            
