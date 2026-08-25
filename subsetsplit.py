from functools import cache
class Solution:
    def minDifference(self, arr: list[int]):
        if arr == []:
            return 0
        if len(arr) == 1:
            return arr[0]
        print(arr)
        s = sum(arr)
        t = int((s/2)+1)
        # print(t)
        n = len(arr)
        dp: list[list[bool]] = [[False] * t for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = True
        for j in range(1, t):
            dp[0][j] = arr[0] == j

        for i in range(1, n):
            for j in range(1, t):
                if arr[i] <= j:
                    dp[i][j] = dp[i-1][j-arr[i]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        for j in range(t-1, -1, -1):
            if dp[n-1][j]:
                return s - 2*j

s = Solution()

print(s.minDifference([1, 2, 3, 4, 5]))
#output should be 1
print(s.minDifference([1, 2, 3, 4, 5, 6]))
#output should be 1
print(s.minDifference([1,6,11,5]))
#output should be 1
print(s.minDifference([1,4]))
#output should be 3
print(s.minDifference([1]))
#output should be 1
print(s.minDifference([1,2,3,4]))
#output should be 1
