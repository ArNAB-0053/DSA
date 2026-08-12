## Lowest Common Ancestor (LCA)

### Binary Tree
- No ordering property → we don't know where `p` and `q` are.
- Recursively search **both left and right subtrees**.
- If both sides return a node → current node is the **LCA**.
- If only one side returns → LCA is in that subtree.

### Binary Search Tree (BST)
- Has an ordering property → we know where `p` and `q` can be.
- Move **left/right based on values**.
- No need to search both subtrees.

### Key Difference
**BT → Search both sides**  
**BST → Use ordering to choose a side**