def fn(num):
    count_t = 0
    while num%2 == 0:
        count_t+=1
        num//=2
    return count_t
test = int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    t = 1
    for num in arr:
        t*=num
    ini = fn(num)
    ans , ind = 0 , 0
    ls = []
    while ind < n:
        ls.append(fn(ind))
        ind += 2
    ls.sort(reverse=True)
    if ini < n:
        for num in ls:
            ini += num
            ans += 1
            if ini >= n:
                print(ans)
                break
        else:
            print(-1)
    else:
        print(ans)
    
        
    

            