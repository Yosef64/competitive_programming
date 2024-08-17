class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        n , m = len(s) , len(t)
        def dp(fInd,sInd):
            if fInd == n or sInd == m:
                # print(fInd,sInd)
                return int(sInd == m)
            
            if (fInd,sInd) in memo:
                print(memo[(fInd,sInd)],(fInd,sInd))
                return memo[(fInd,sInd)]
            num = 0
            for i in range(fInd,n):
                if s[i] == t[sInd]:
                    memo[(i,sInd)] = dp(i+1,sInd+1)
                    # print(memo[(i,sInd)],(i,sInd))
                    num += memo[(i,sInd)]
            # print(num,fInd)
            return num
        return dp(0,0)