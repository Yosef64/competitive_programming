def fn(arr):
    ind = len(arr) - 1
    while ind > 0:
        if abs(arr[ind]-arr[ind-1]) > 1:
            return False
        ind -= 1
    return True

test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    print("YES" if fn(sorted(arr)) else "NO")