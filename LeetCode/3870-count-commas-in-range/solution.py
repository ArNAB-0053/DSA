class Solution:
    def countCommas(self, n: int) -> int:
        ## Normal approach
        # l = len(str(n))

        # if l < 4:
        #     return 0
        
        # if l == 4:
        #     return n - 1000 + 1
        
        # if l > 4:
        #     return int("9" * (l-4) + "000") * (l // 3 if l % 3 != 0 else l // 3 - 1) + (n - 10 ** (l-1)) + 1

        ## Optimal approach
        p = 1000
        ans = 0
        while p <= n:
            ans += n - p + 1
            p *= 1000

        return ans
