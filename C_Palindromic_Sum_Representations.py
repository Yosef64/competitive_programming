t = int(input())
amount = 4 * (10 ** 4)
row = [0 for _ in range(amount+1)]
row[0] = 1
coins = [i for i in range(1,amount + 1) if str(i) == str(i)[::-1]]
for coin in coins:
    for amt in range(coin,amount+1):
        row[amt] += row[amt-coin] % (10 ** 9 + 7)
for _ in range(t):   
    n = int(input())
    
    print(row[n] % (10 ** 9 + 7))
