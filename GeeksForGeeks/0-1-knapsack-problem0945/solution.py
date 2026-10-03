class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        
        # dp = [[0] * (W+1) for _ in range(n+1)]
        
        # for i in range(1, n+1):
        #     for j in range(1, W+1):
        #         if wt[i-1] <= j:
        #             dp[i][j] = max(
        #                 val[i-1] + dp[i-1][j - wt[i-1]],
        #                 dp[i-1][j]
        #             )
        #         else:
        #             dp[i][j] = dp[i-1][j]

        # return dp[n][W]
        
        # OBSERVATION:
        # dp[i][j] only depends on prevous i and changing j
        # means i not actually not changing in a weird way, 
        # and if we can track the previous i that will be enough 
        # and don't have to store it.
        # so, we can reduce 2D matrix to a 1D array
        
        dp = [0] * (W+1)
        
        for i in range(1, n+1):
            for j in range(W, 0, -1):
                if wt[i-1] <= j:
                    dp[j] = max(
                        val[i-1] + dp[j - wt[i-1]],
                        dp[j]
                    )
                    
        return dp[W]