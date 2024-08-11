from collections import defaultdict


test = int(input())
for _ in range(test):
    n , c = map(int,input().split())
    arr = list(map(int,input().split()))
    orbits = defaultdict(int)
    for orbit in arr:
        orbits[orbit] += 1
    
    ans = 0
    for key in orbits:
        ans += min(c,orbits[key])
    print(ans)