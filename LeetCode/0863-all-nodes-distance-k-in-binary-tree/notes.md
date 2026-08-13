## Intuition

All approaches use the same basic idea:

1. Treat the binary tree as an **undirected graph** so we can move both up and down.
   - First two approaches: explicitly store both `parent -> child` and `child -> parent`.
   - Third approach: store only `child -> parent` and use `left`/`right` directly for downward movement, avoiding the full adjacency list.

2. Start BFS from the `target` because every edge has a distance of `1`.

3. We only need nodes at distance `K`, so stop BFS after reaching the `Kth` level.

4. At distance `K`, the nodes currently in the queue are exactly the answer.

### Why the third approach is better

- No need to build a complete adjacency list.
- Only store the `parent` of each node.
- `left` and `right` already give us the downward connections.
- Same `O(n)` time and `O(n)` space, but less extra graph data.

### Why the Parent Map approach is lighter

- Explicit graph stores every edge in both directions.
- Parent map stores only `child -> parent`.
- `left` and `right` are already stored in the tree, so we reuse them.
- Same `O(n)` time and `O(n)` space, but less extra memory in practice.