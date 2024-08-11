test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    arr = [[arr[ind],ind] for ind in range(n)]
    arr.sort(key= lambda x:x[0])
    # print(arr)
    dp = [0] * n
    pre , count , i = 0, 0,0
    for ele, ind in arr:
       
        if ind > i:
            i = ind
        while (i < n and arr[i][0] <= pre) or not pre:
            pre += arr[i][0]
            count += 1
            i += 1
        dp[ind] = str(count - 1)
    print(" ".join(dp))