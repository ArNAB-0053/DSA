class Solution:
    def isSubsetSum(self, arr: list[int], summ: int) -> bool:
        n = len(arr)
        dp = [ [False] * (summ + 1) for _ in range(n+1) ]
        
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(1, n+1):
            for j in range(1, summ + 1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
                    
        return dp[n][summ]
        
        