count , l = 0 , 0
listArray = [5, 10, 15, 20]
limit ,divisor = 4, 5 
unique = set()
for r in range(len(listArray)):
    if listArray[r] % divisor:
        l = r + 1
        continue
    wins = r
    while wins >= l and wins >= r - limit + 1:
        tup = tuple(listArray[wins:r+1])
        if tup not in unique:
            unique.add(tup)
            count += 1
        wins -= 1
            
print(count)     
        
    
    