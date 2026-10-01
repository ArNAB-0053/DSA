class Solution:
    def fib(self, n: int) -> int:
        # base cases
        if n == 0: return 0
        if n == 1: return 1

        # initializing dp
        dp = [-1] * (n+1)
        # base cases
        dp[0] = 0
        dp[1] = 1
        # recursive fn
        def solve(n):
            # early return
            if dp[n] != -1:
                return dp[n]
            # recursion call
            dp[n] = solve(n-1) + solve(n-2)
            return dp[n]
        return solve(n)