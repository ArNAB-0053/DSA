class Solution:
    def isSubsetSum(self, arr: list[int], summ: int) -> bool:
        n = len(arr)
        
        # ------------------------------------------
        # USING 2D DP
        # ------------------------------------------
        # dp = [ [False] * (summ + 1) for _ in range(n+1) ]
        
        # for i in range(n+1):
        #     dp[i][0] = True
            
        # for i in range(1, n+1):
        #     for j in range(1, summ + 1):
        #         if arr[i-1] <= j:
        #             dp[i][j] = dp[i-1][j - arr[i-1]] or dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j]
                    
        # return dp[n][summ]
        
        # ------------------------------------------
        # USING 1D ARRAY
        # ------------------------------------------
        # OBSERVATION:
        # to contruct the answer dp[i][j], it only needs previous i and
        # 
        # so we can reduce 2D matrix to a 1D array
        
        dp = [False] * (summ + 1)
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(summ, 0, -1):
                if arr[i-1] <= j:
                    dp[j] = dp[j - arr[i-1]] or dp[j]
        return dp[summ]
        
        