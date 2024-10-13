n = int(input())
t = list(map(int,input().split()))
arr = []
def findInd(tar):
    l , r = 0 , len(arr) - 1
    while l < r:
        mid = (r - l)//2 + l
        
        if arr[mid][-1] > tar:
            l = mid + 1
        else:
            r = mid
    return l
for num in t:
    ind = findInd(num)
    if not arr or arr[ind][-1] > num:
        arr.append([num])
    else:
        arr[ind].append(num)
        
for ls in arr:
    print(" ".join(map(str,ls)))
        