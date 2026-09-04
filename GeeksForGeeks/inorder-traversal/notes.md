## Morris Traversal Technique

Binary tree traversal can be done using **Recursion**, **Stack**, or **Morris Traversal**.

**Morris Traversal** is a **space-optimized traversal technique** that uses **O(n) time and O(1) extra space**.

- Recursion / Stack → **O(n) time, O(h) space**
- Morris Traversal → **O(n) time, O(1) space**

> **Key Idea:** Create a **temporary thread (link)** between nodes to traverse the tree without using a stack or recursion. The thread is removed after use to restore the original tree.