## 2 Approaches

- **Recursive Approach:** If both nodes are smaller, move left; if both are greater, move right; otherwise, current node is the LCA.
  - **TC:** `O(h)` - best/average, `O(n)` - worst
  - **SC:** `O(h)` - recursion stack

- **Iterative Approach:** Use a `while` loop with the same logic as recursion, avoiding recursion stack space.
  - **TC:** `O(h)` - best/average, `O(n)` - worst
  - **SC:** `O(1)`