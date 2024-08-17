test = int(input())
ans , memo = float("inf") , {}
def dp(d,i,removed,s):
    global ans,memo
    if i == len(s):
        if d and not int(d)%25:
            ans = min(ans,removed)
        return 
    
    dp(d+s[i],i+1,removed,s)
    dp(d,i+1,removed+1,s)
    return 

for _ in range(test):
    digit = input()
    dp("",0,0,digit)
    print(ans)
    ans = float("inf")
    
    