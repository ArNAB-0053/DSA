class Solution:
    def minCost(self, height: list[int]) -> int:
        n = len(height) - 1
        
        # frog is in the last stair 
        if n < 1:
            return 0 
        # # dp creation
        # dp = [-1] * (n + 1)
        # # dp initialization
        # dp[0] = 0
        # # there is not other way to reach index 1 except from 0th index
        # dp[1] = abs(height[1] - height[0]) 
        # # def solve(n):
        # #     # early return
        # #     if dp[n] != -1:
        # #         return dp[n]
            
        # #     dp[n] = min(
        # #         solve(n-1) + abs(height[n] - height[n-1]), # jumps i+1
        # #         solve(n-2) + abs(height[n] - height[n-2])  # jumps i+2
        # #     )
            
        # #     return dp[n]
        # # solve(n)
        # # return dp[n]
        
        # for i in range(2, n+1):
        #     if dp[i] == -1:
        #         dp[i] = min(
        #             dp[i-1] + abs(height[i] - height[i-1]),
        #             dp[i-2] + abs(height[i] - height[i-2])
        #         )
        # return dp[n]
        
        pprev, prev = 0, abs(height[1] - height[0]) 
        for i in range(2, n+1):
            temp = prev
            prev = min(
                prev + abs(height[i] - height[i-1]),
                pprev + abs(height[i] - height[i-2])
            )
            pprev = temp
            
        return prev
        