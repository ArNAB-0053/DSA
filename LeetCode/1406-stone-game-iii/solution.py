class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        ## recursion + memo || TC: O(n) | SC: O(n)
        # t = [float('-inf')] * n
        # @cache
        # def solve(i):
        #     if i >= n: return 0
        #     if t[i] != float('-inf'): return t[i]
        # res = stoneValue[i] - solve(i+1)
        # if i+1 < n:
        #     res = max(res, stoneValue[i] + stoneValue[i+1] - solve(i+2))
        # if i+2 < n:
        #     res = max(res, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - solve(i+3))

        #     t[i] = res
        #     return res

        # diff = solve(0)


        ## bottom-up DP || TC: O(n) | SC: O(n)
        # dp = [0] * (n+1)

        # for i in range(n-1, -1, -1):
        #     dp[i] = stoneValue[i] - dp[i+1]
        #     if i+2 <= n:
        #         dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] - dp[i+2])
        #     if i+3 <= n:
        #         dp[i] = max(dp[i], stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i+3])

        # diff = dp[0]

        # for both recursion and bottom-up
        # if diff > 0:
        #     return "Alice"
        # if diff < 0:
        #     return "Bob"
        # else:
        #     return "Tie"


        ## Observation
        ## there is only 3 items that are changing i+1, i+2, i+3
        # TC: O(n) | SC: O(1)
        a = b = c = 0 # a -> i+1, b -> i+2, c -> i+3
        for i in range(n-1, -1, -1):
            res = float('-inf')
            res = stoneValue[i] - a
            if i+1 < n:
                res = max(res, stoneValue[i] + stoneValue[i+1] - b)
            if i+2 < n:
                res = max(res, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - c)

            # as this is reverse loop, we are going backward
            # so i+m will be become i+m-1 || m -> 1,2,3 ...
            # i+3 -> i+2 => c = b
            # i+2 -> i+1 => b = a
            # i+1 -> i; now in bottom-up version we know dp[i] stores the result, so here a = res
            # a will carry this phase's result to next phase
            c, b, a = b, a, res
        # as a carries the last result
        if a > 0:
            return "Alice"
        if a < 0:
            return "Bob"
        else:
            return "Tie"