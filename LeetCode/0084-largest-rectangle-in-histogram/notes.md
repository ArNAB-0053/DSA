### Approach 1: N.S.L + N.S.R
- Find **Nearest Smaller Left** and **Nearest Smaller Right** for each bar.
- Calculate `width = right - left - 1`, then `area = height × width`.
- **Most straightforward / easiest to derive.**

### Approach 2: One-Pass Monotonic Stack
- Store `(index, height)` in stack.
- Calculate the area **when popping** a bar.
- Remaining bars extend to the end.

### Approach 3: One-Pass Stack + Sentinel `0`
- Append `0` to force all remaining bars to pop.
- Calculate area while popping.
- **Cleanest implementation.**

### Complexity
- **TC:** `O(n)` — all approaches
- **SC:** `O(n)` — all approaches

> **Remember:** 
> Approach 1 is easiest to derive from basic N.S.L/N.S.R.  
> Approach 3 is the cleanest implementation.