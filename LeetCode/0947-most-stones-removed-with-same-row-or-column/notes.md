### DSU Approach

#### Steps

1. Treat each **row** and **column** as a DSU node.
2. Shift column indices by `maxRow + 1` so row and column nodes do not overlap.
3. For every stone `(row, col)`, union `row` and `shifted_col`.
4. Track all row/column nodes that actually appear in stones using a `used` set.
5. Count the number of connected components by counting roots among the used nodes.
6. If a component contains `k` stones, we can remove `k - 1` stones.
7. Therefore, the maximum number of removable stones is:

   `total_stones - number_of_components`

#### Complexity

* Time: `O(N · α(N))`
* Space: `O(maxRow + maxCol)`

where `α(N)` is the inverse Ackermann function (almost constant).

> _Go through the code for better understanding_
