- Floyd Warshall
- Dijkstra from every vertex

### Floyd Warshall
- Creates complete shortest-path distance matrix.
- Time Complexity: `O(V³)`
- Works even with negative edges (but no negative cycles).
- Overkill here since all edge weights are positive.

### Dijkstra for All Vertices
- Run Dijkstra from each city.
- Count cities reachable within `distanceThreshold`.
- Time Complexity: `O(V * E log V)`
- Better for sparse graphs.
- Preferred approach when there are no negative edges.

### Key Observation
- Floyd Warshall is accepted but expensive.
- Since all weights are positive, repeated Dijkstra is a more optimized solution.