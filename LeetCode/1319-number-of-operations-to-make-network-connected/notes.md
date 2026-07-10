### Approach : `Disjoint Set Union(DSU)`

#### Why  `cntComp - 1` is answer or in the early check, checking `len(connections) < n-1` ?

- Suppose there are k disconnected components.
- One edge can connect two components.
- Every time we add an edge between two different components, the number of components decreases by 1.

**Example:**
```text
4 components
↓ add 1 edge
3 components
↓ add 1 edge
2 components
↓ add 1 edge
1 component
```

Therefore, to connect k components into a single connected network,
we need exactly `k - 1` edges.

`Answer = components - 1`