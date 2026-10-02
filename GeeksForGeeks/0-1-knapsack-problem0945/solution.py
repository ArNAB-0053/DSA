class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        n = len(val)
        
        dp = [[0] * (W+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    dp[i][j] = max(
                        val[i-1] + dp[i-1][j - wt[i-1]],
                        dp[i-1][j]
                    )
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][W]