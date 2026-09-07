## Approach

- **Preorder + Upper Bound:** Use preorder traversal with an index `i` and a `maxx` boundary.
  - Create the current node from `preorder[i]` if it is within the allowed range.
  - **Left subtree:** `maxx = node.val` because left values must be smaller than the parent.
  - **Right subtree:** `maxx` remains unchanged because right values only need to be smaller than the ancestor's upper bound.
  - If `preorder[i] > maxx`, return `None` without moving `i`, so the value can be processed by the appropriate ancestor.
  
- **TC:** `O(n)` - each preorder element is processed once
- **SC:** `O(h)` - recursion stack