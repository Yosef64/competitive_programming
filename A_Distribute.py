n = int(input())
arr = list(map(int,input().split()))
arr = [[val,ind+1] for ind , val in enumerate(arr)]
arr.sort()
left , right = 0 , n - 1
while left < right :
    print(arr[left][1],arr[right][1])
    left , right = left + 1, right - 1