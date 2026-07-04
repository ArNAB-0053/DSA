## Intuition

- `x, y` represent the **top-left corner** of the square submatrix.
- `k` represents the **side length** of the square.
- Therefore:

```text
Rows: x ........ x + k - 1
Cols: y ........ y + k - 1
```

Example:

```
k = 3

          y     y+1    y+2
x         *      *      *
x+1       *      *      *
x+2       *      *      *

last row = x + k - 1
last col = y + k - 1
```

> Key observation:
>
> ```text
> start index + length - 1 = last index
> ```
>
> This pattern appears in subarrays, matrix regions, sliding windows, etc.

### Why `x + k - 1`?

> This the key obervation -
> ```text
> start index + length - 1 = last index
> ```

Example:

```text
x = 2
k = 2

Selected rows:
2
3
```

Last row is:

```text
2 + 2 - 1 = 3
```

not `4`.

So the selected square always spans:

```text
[x, x + k - 1]
[y, y + k - 1]
```