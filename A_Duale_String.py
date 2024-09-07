test = int(input())
for _ in range(test):
    st = input() 
    n = len(st)
    if len(st) > 1 and st[:n//2] == st[n//2:]:
        print("YES")
    else:print("NO")
        