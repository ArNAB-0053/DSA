### Approach 1: DSU 
_`This is actually better space complexity wise`_
```
TC: O((V + E)·α(V)) ≈ O(V + E)
SC: O(V)
```

---

### Approach 2: DFS/BFS + edge and vertices count for all components
_`But this is easy to remember and code-wise very simple`_

```
TC: O(V + E)
SC: O(V + E)
```

#### Intuition : 
- Just go for each connected component 
- count the number of edges and vertices
- if `edges = vertices * (vertices - 1) // 2` then increase the count by `1`