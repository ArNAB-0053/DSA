#### Memory Limit Exceeded (Dict DP)

**Main Problem**
- Used a dictionary with tuple keys `(i, first, second)`.
- Tabulation fills every state, making the state space dense.
- Dictionary entries have significant memory overhead due to hashing and tuple storage.

**What to Learn**
- Dictionaries work well for sparse memoization where only visited states are stored.
- For dense tabulation, arrays/lists are usually more memory efficient.

**Next Improvement**
- Replace the dictionary with a 3D DP array.

```python
import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)
        mx = max(nums)

        dp = {}

        # base case
        for first in range(mx+1):
            for second in range(mx+1):
                nonZero = first != 0 and second != 0
                gcdMatch = first == second

                dp[(n,first,second)] = 1 if nonZero and gcdMatch else 0

        for i in range(n-1, -1, -1):
            for first in range(mx, -1, -1):
                for second in range(mx, -1, -1):
                    skip = dp[(i+1,first,second)]
                    take1 = dp[(i+1, math.gcd(first, nums[i]), second)]
                    take2 = dp[(i+1, first, math.gcd(second, nums[i]) )]
                    dp[(i, first, second)] = (skip % MOD + take1 % MOD + take2 % MOD) % MOD

        return dp[(0, 0, 0)]
```

---

#### 3D DP

**Main Problem**
- Stores all `n + 1` DP layers.
- Each state only depends on the next layer (`i + 1`), so most of the stored layers are unnecessary.

**Observation**
- The transition only requires information from one future layer.

**Next Improvement**
- Compress the `i` dimension using rolling arrays (`prev` and `curr`).

```python
import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)
        mx = max(nums)

        dp = [ [  [0] * (mx+1) for _ in range(mx+1) ] for _ in range(n+1) ]

        # base case
        for first in range(mx+1):
            for second in range(mx+1):
                nonZero = first != 0 and second != 0
                gcdMatch = first == second

                dp[n][first][second] = 1 if nonZero and gcdMatch else 0

        for i in range(n-1, -1, -1):
            for first in range(mx, -1, -1):
                for second in range(mx, -1, -1):
                    skip = dp[i+1][first][second]
                    take1 = dp[i+1][math.gcd(first, nums[i])][second]
                    take2 = dp[i+1][first][math.gcd(second, nums[i])]
                    dp[i][first][second] = (skip % MOD + take1 % MOD + take2 % MOD) % MOD

        return dp[0][0][0]
```

---

#### 2D DP (Space Optimized)

**Improvement**
- Reduced memory usage from `O(n × mx²)` to `O(mx²)` by keeping only the current and next DP layers.

**Main Problem**
- Still performs repeated `gcd` computations for every DP state.

**Observation**
- The same GCD values are calculated many times across transitions.

**Next Improvement**
- Precompute all possible GCD values and replace repeated function calls with table lookups.

```python
import math

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        n = len(nums)
        mx = max(nums)

        prev = [ [0] * (mx+1) for _ in range(mx+1) ]

        # base case
        for first in range(mx+1):
            for second in range(mx+1):
                nonZero = first != 0 and second != 0
                gcdMatch = first == second
                prev[first][second] = 1 if nonZero and gcdMatch else 0

        for i in range(n-1, -1, -1):
            curr = [ [0] * (mx+1) for _ in range(mx+1) ]
            for first in range(mx, -1, -1):
                for second in range(mx, -1, -1):
                    skip = prev[first][second]
                    take1 = prev[math.gcd(first, nums[i])][second]
                    take2 = prev[first][math.gcd(second, nums[i])]
                    curr[first][second] = (skip % MOD + take1 % MOD + take2 % MOD) % MOD
            prev = curr

        return prev[0][0]
```

---

#### More Optimized (2D DP + Precomputed GCD)

**Improvement**
- Eliminated repeated `gcd` computations by using a precomputed lookup table.
- Reduced the constant factor in the DP transitions.

**Complexity**
- Time: `O(n × mx²)`
- Space: `O(mx²)`

**Remaining Observation**
- The total number of DP states remains unchanged.
- This optimization improves runtime but does not change the overall time complexity.

**Possible Further Improvement**
- Investigate sparse-state DP approaches that process only reachable GCD states instead of iterating through the entire state space.

```python
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
```