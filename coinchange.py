class Solution:
    def minCoins(self, coins: list[int], sum: int) -> int:
        n = len(coins)
        dp = [[float('inf')]*(sum+1) for _ in range(n+1)]
        
        dp[n][0] = 0
        for i in range(n+1):
            dp[i][0] = 0

        for i in range(n-1,-1,-1):
            for j in range(1,sum+1):
                dp[i][j] = dp[i+1][j]
                if j>= coins[i]:
                    dp[i][j] = min(
                        dp[i+1][j],
                        dp[i][j-coins[i]]+1)
        print(dp)
        if dp[0][sum] == float('inf'):
            return -1
        else:
            return dp[0][sum]
        # code here
        # dp = {}
        # def backtrack(i,T):
        #     if T < 0:
        #         return float('inf')
        #     if i == len(coins):
        #         if T == 0:
        #             return 0
        #         else:
        #             return float('inf')
        #     if (i,T) in dp:
        #         return dp[(i,T)]
        #     dp[(i,T)] =  min(
        #         backtrack(i+1, T),
        #         backtrack(i, T-coins[i])+1
        #         )
        #     return dp[(i,T)]
        
        # c = backtrack(0, sum)
        # if c == float('inf'):
        #     return -1
        # else:
        #     return c

s = Solution()
# print(s.minCoins([25,10,5], 30))
print(s.minCoins([3,6,9], 6))