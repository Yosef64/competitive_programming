n = int(input())
arr = list(map(int,input().split()))
count = 0
for ind in range(n - 2 ,-1,-1):
    i = ind 
    # print(i)
    while i < n -1 and arr[i] > arr[i+1]:
        diff = arr[i] - arr[i+1]
        # print(diff)
        arr[i] , arr[i+1] = arr[i] - diff ,arr[i+1] + diff
        i += 1
print(" ".join(map(str,arr)))
        