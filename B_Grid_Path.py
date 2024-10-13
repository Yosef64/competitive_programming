'''
There is a n×m
 grid. You are standing at cell (1,1)
 and your goal is to finish at cell (n,m)
.

You can move to the neighboring cells to the right or down. In other words, suppose you are standing at cell (x,y)
. You can:

move right to the cell (x,y+1)
 — it costs x burles;
move down to the cell (x+1,y)
 — it costs y burles.
Can you reach cell (n,m)
 spending exactly k
 burles?

'''
def fn(n,m,k):
    dp = [[0 for c in range(m)] for _ in range(n)]
    for i in range(m-2,-1,-1):
        dp[-1][i] = dp[-1][i+1] + i + 1
    
    for i in range(n-2,-1,-1):
        for col in range(m-1,-1,-1):
            if col < m - 1:
                if dp[i][col+1] < dp[i+1][col]:
                    dp[i][col] = dp[i][col+1] + i + 1
                else:
                    dp[i][col] = dp[i][col] + col + 1
            else:
                dp[i][col] = dp[i+1][col] + i + 1
    return dp[0][0] == k



