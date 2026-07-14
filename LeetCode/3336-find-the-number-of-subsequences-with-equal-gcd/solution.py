import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)
        mx = max(nums)

        prev = [ [0] * (mx+1) for _ in range(mx+1) ]
        gcd = [ [0] * (mx+1) for _ in range(mx+1) ]

        # base case
        for first in range(mx+1):
            for second in range(mx+1):
                nonZero = first != 0 and second != 0
                gcdMatch = first == second
                prev[first][second] = 1 if nonZero and gcdMatch else 0

        # computing GCP
        for a in range(mx+1):
            for b in range(mx+1):
                gcd[a][b] = math.gcd(a,b)

        for i in range(n-1, -1, -1):
            curr = [ [0] * (mx+1) for _ in range(mx+1) ]
            for first in range(mx, -1, -1):
                for second in range(mx, -1, -1):
                    skip = prev[first][second]
                    take1 = prev[gcd[first][nums[i]]][second]
                    take2 = prev[first][gcd[second][nums[i]]]
                    curr[first][second] = (skip + take1 + take2) % MOD
            prev = curr

        return prev[0][0]