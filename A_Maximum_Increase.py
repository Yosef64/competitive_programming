n = int(input())
arr = list(map(int,input().split()))

count ,ans = 1 , 0
for i in range(1,n):
    if arr[i] > arr[i -1]:
        count+= 1
    else:
        ans = max(ans,count)
        count = 1
ans = max(ans,count)
print(ans)
        
