test = int(input())
for _ in range(test):
    f , s = list(map(int,input().split()))
    print(min(f,s),max(f,s))