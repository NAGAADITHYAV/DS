# from functools import cache
# commeted out the recusion dp solution
class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        # code here
        # @cache
        n = len(val)
        dp = [[0]*(W+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, W+1):
                dp[i][j] = dp[i-1][j]
                if wt[i-1] <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-wt[i-1]]+val[i-1])
        # print(dp)
        return dp[-1][-1]

        # def backtrack(i, cap):
        #     if (i, cap) in dp:
        #         return dp[(i, cap)]
        #     if cap < 0:
        #         dp[(i, cap)] = float('-inf')
        #         return dp[(i, cap)]
        #     if i < 0:
        #         dp[(i, cap)] = 0
        #         return dp[(i, cap)]
        #     dp[(i, cap)] = max(
        #         backtrack(i-1, cap),
        #         backtrack(i-1, cap-wt[i]) + val[i]
        #     )
        #     return dp[(i, cap)]
        
        # return backtrack(len(wt)-1,W)

s= Solution()
print(s.knapsack(4, [1,2,3], [4,5,1]))
#3
print(s.knapsack(3, [1,2,3], [4,5,6]))
#0
print(s.knapsack(5, [10,40,30,50], [5,4,2,3]))
#80