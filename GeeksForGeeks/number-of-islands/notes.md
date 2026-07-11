Approach:
- Use DSU to dynamically maintain connected components (islands).
- Treat every new land cell as a new island (cnt += 1).
- Check its 4 neighbors; if a neighboring land belongs to a different component, union them and decrement the island count.
- Store the current island count after each operation.

```
TC: O(k · α(rows * cols))
SC: O(rows * cols)
```

> Code comments contain the detailed intuition and implementation steps.