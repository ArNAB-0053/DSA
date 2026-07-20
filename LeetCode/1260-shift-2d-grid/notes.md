## Intuition

Although the input is a **2D grid**, the shifting operation behaves exactly like shifting a **1D array**.

For example,

```
1 2 3
4 5 6
7 8 9
```

can be viewed as

```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

A right shift by one becomes

```
[9, 1, 2, 3, 4, 5, 6, 7, 8]
```

which corresponds to

```
9 1 2
3 4 5
6 7 8
```

Instead of actually flattening and rotating the array, we can directly calculate the new position of every element using index mapping.

---

## Key Observation

Every cell `(row, col)` has a corresponding **1D index**.

```
index = row * cols + col
```

For a grid with `cols = 3`,

```
Grid

1 2 3
4 5 6

Indices

0 1 2
3 4 5
```

---

## After Shifting

If an element is originally at index

```
idx
```

then after shifting right by `k` positions,

```
newIndex = (idx + k) % totalElements
```

The modulo is required because elements that move past the last position wrap around to the beginning.

Example:

```
totalElements = 6

idx = 5
k = 2

newIndex = (5 + 2) % 6
         = 1
```

---

## Convert Back to 2D

Once the new 1D index is known, convert it back into row and column.

```
newRow = newIndex // cols
newCol = newIndex % cols
```

Example:

```
cols = 3
newIndex = 4

newRow = 4 // 3 = 1
newCol = 4 % 3 = 1
```

So index `4` corresponds to

```
1 2 3
4 5 6
  ↑
(row = 1, col = 1)
```

---

## Algorithm

1. Compute the total number of elements.
2. Reduce `k` using modulo.
3. Create an empty answer grid.
4. Traverse every cell.
5. Convert its `(row, col)` into a 1D index.
6. Compute its shifted index.
7. Convert the shifted index back into `(row, col)`.
8. Place the element in its new position.

---

## Why does this work?

The grid is stored in **row-major order**.

Moving one step to the right in the grid is exactly the same as moving one position forward in its 1D representation.

Therefore, every element can be moved by simply updating its 1D index and converting it back to a 2D position.

---

## Complexity

**Time:** O(rows × cols)

Every cell is visited exactly once.

**Space:** O(rows × cols)

An additional grid is created to store the shifted result.