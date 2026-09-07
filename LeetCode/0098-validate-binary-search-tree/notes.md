## 2 Approaches

- **Min-Max Approach:** Modify the `min` and `max` range based on whether we move left or right.
- **Optimized Inorder Approach:** Inorder traversal of a BST gives values in sorted order. Keep track of the previous value and return `false` if `prev >= current`.