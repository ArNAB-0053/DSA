**`Hard observation problem.`**

---

Key idea:
- Treat concatenation as a rolling hash.
- Store prefix concatenated value of non-zero digits.
- Store prefix count of non-zero digits.
- Store powers of 10 modulo MOD.
- Range concatenation:
  pref[r] - pref[l-1] * 10^(nonZeroCount)

Complexity:
O(n + q) time
O(n) space

This is the optimal asymptotic solution.

> **NOTE:**
> - Need more practice with this pattern; otherwise, it's easy to forget the approach.
> - This is a *math-heavy* solution involving several low-level mathematical observations and modular arithmetic tricks that are difficult to retain without regular practice.