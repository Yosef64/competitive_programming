from collections import Counter


test = int(input())
for _ in range(test):
    n = int(input())
    log , ans = Counter(input()) , 0
    for key in log:
        
        if ord(key.lower()) - 96 <= log[key]:
            ans += 1
    print(ans)
        
    