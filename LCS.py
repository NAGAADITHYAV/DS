class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str):
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return dp[m][n]
        res = []
        i, j = m, n
        while(i>0 and j>0):
            if text1[i-1] == text2[j-1]:
                res.append(text1[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
        return ''.join(reversed(res))
        # def backtrack(i, j):
        #     if dp[i+1][j+1] is not None:
        #         return dp[i+1][j+1]
        #     if text1[i] == text2[j]:
        #         dp[i+1][j+1] = 1+backtrack(i-1, j-1)
        #         return dp[i+1][j+1]
        #     dp[i+1][j+1] =max( backtrack(i-1, j), backtrack(i, j-1))
        #     return dp[i+1][j+1]

        # return backtrack(m-1, n-1)
        
s = Solution()
print(s.longestCommonSubsequence('abc', 'ab'))