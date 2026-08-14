## Intuition

- Store `parent` for every node so we can move **up** the tree.
- Now we can treat the tree like an **undirected graph**: `parent`, `left`, and `right`.
- Start from the target and use **BFS**, where each level represents 1 unit of distance.
- The last level reached gives the **maximum distance from the target**, which is the burning time.