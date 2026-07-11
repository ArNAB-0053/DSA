_**```NEED PRACTISE```**_


#### Approach 1 : DSU
1. Use DSU to form connected components of all existing land cells.
2. For every water cell (0), simulate flipping it to 1 and combine the sizes of all unique neighboring islands.
3. Take the maximum possible size.
4. Handle the all-1s case by returning the largest existing component.

```
TC: O(N² · α(N²))
SC: O(N²)
```

#### Approach 2 : DFS
1. Traverse the grid and label every island with a unique id (2, 3, 4, ...).
2. Store the size of each island in a hashmap: island_id → size.
3. For every water cell (0), gather all unique neighboring island ids.
4. Sum the sizes of those islands and add 1 for the flipped cell.
5. Track the maximum possible island size.
6. Handle the all-1s case by returning the size of the largest existing island.

```
TC: O(N²)
SC: O(N²)
```

**Revision Trigger**
> DSU  -> Think "components + component sizes".
> DFS  -> Think "island id labeling + hashmap of sizes".