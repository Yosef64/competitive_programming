import math
n , k = list(map(int,input().split()))
if k % 2 == 0:
    print(-1)
    exit()
arr = [ind for ind in range(1, n+1)]
def mergeSort(l ,r):
    global k,arr
    if k == 1 or l == r: return True
    mid = (r - l) // 2 + l
    k -= 2
    lc = mergeSort(l , mid)
    rc = mergeSort(mid + 1 , r)
    if lc and rc:
        arr[l] , arr[l+1]  = arr[l+1],arr[l]
    
    return False

res= mergeSort(0,n-1)
print(" ".join(map(str,arr)))
        