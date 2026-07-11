_**```NEED PRACTISE```**_


#### Approach:
1. Use DSU to form connected components of all existing land cells.
2. For every water cell (0), simulate flipping it to 1 and combine the sizes of all unique neighboring islands.
3. Take the maximum possible size.
4. Handle the all-1s case by returning the largest existing component.

```
TC: O(N² · α(N²))
SC: O(N²)
```