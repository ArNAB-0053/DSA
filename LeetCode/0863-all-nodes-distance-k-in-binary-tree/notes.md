## Intuition

Both approaches use the same basic idea:

1. Convert the binary tree into an undirected graph using an adjacency list. Store the connection in both directions: `parent -> child` and `child -> parent`.

2. Once we have the graph, treat the target node as the starting point and use BFS because every edge has a distance of 1.

 3. We only care about nodes at distance K from the target, so there is no need to continue BFS after reaching the Kth level.

 4. After reaching distance K, the nodes currently in the queue are exactly the nodes we need, so return their values.