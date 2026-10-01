class Solution:
    def fib(self, n: int) -> int:
        ## ++++++++++++++++++++++++++++++++++++++++++++++
        ## Recursion + Memoization
        ## TC: O(n) | SC: O(n) [Recursion Stack] + O(n) [main array] -> O(2n) -> O(n)
        ## ++++++++++++++++++++++++++++++++++++++++++++++
        # # base cases
        # if n == 0: return 0
        # if n == 1: return 1

        # # initializing dp
        # dp = [-1] * (n+1)
        # # base cases
        # dp[0] = 0
        # dp[1] = 1
        # # recursive fn
        # def solve(n):
        #     # early return
        #     if dp[n] != -1:
        #         return dp[n]
        #     # recursion call
        #     dp[n] = solve(n-1) + solve(n-2)
        #     return dp[n]
        # return solve(n)

        ## ++++++++++++++++++++++++++++++++++++++++++++++
        ## Tabulation
        ## TC: O(n) | SC: O(n) 
        ## ++++++++++++++++++++++++++++++++++++++++++++++
        # # base cases
        # if n == 0 or n == 1: return n
        # # initializing dp
        # dp = [-1] * (n+1)
        # # base cases
        # dp[0], dp[1] = 0, 1
        # # main loop for tabulation
        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # # returning the result
        # return dp[n]


        ## ++++++++++++++++++++++++++++++++++++++++++++++
        ## BASED ON OBSERVATION
        ## TC: O(n) | SC: O(1)
        ## ++++++++++++++++++++++++++++++++++++++++++++++
        # We only need n-1 and n-2 to compute n
        # so if we only store those, I think we can get the result

        # base cases
        if n == 0 or n == 1: return n

        prev = 1 # n-1 -> base n-1 is 1
        pprev = 0 # n-2 -> base n-2 is 0

        for i in range(2, n+1):
            temp = prev
            prev += pprev
            pprev = temp
        
        return prev