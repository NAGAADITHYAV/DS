class Solution:
    def LIS(self, arr):
        # Code here
        n = len(arr)
        dp = [1]*n
        parse = list(range(n))
        maxi, maxii = 1, -1
        for i in range(n):
            for j in range(i):
                if arr[i]>arr[j] and dp[j]+1 > dp[i]:
                    dp[i] = dp[j]+1
                    parse[i] = j
                    if maxi < dp[i]:
                        maxi = dp[i]
                        maxii = i
        
        res = []
        if maxii == -1:
            return [arr[0]]
        while maxii >=0:
            res.append(arr[maxii])
            if maxii == parse[maxii]:
                break
            maxii = parse[maxii]
        # res.append()
        
        res.reverse()
        return res

s = Solution()
print(s.LIS([10,9,2,5,3,7,101, 18]))
print(s.LIS([0,1,0,3,2,3]))
print(s.LIS([7,7,7,7,7,7,7]))