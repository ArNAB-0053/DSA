`need practise - check code comments as well`

---

## Idea

We use **BFS (level-order traversal)** because the width is calculated for each level.

The tricky part is that **null positions also count**.

For example:

        1
       / \
      2   3
     /     \
    4       5

At the last level, the positions are:

    4   null   null   5

So the width is `4`, not `2`.

To keep track of these positions, we give every node an **index**, like we would do for a complete binary tree.

- Root → index `0`
- Left child → `2 * index + 1`
- Right child → `2 * index + 2`

So the above tree becomes:

        0
       / \
      1   2
     /     \
    3       6

The width of a level is:

    rightmost_index - leftmost_index + 1

For the last level:

    6 - 3 + 1 = 4

---

## Why do we normalize the index?

If the tree is very deep and skewed, the indexes can become extremely large because every level keeps doing:

    2 * index + 1
    2 * index + 2

We don't actually need the **original index value**. We only care about the **relative positions between nodes on the same level**.

So, for every level, we subtract the index of the first node from all indexes.

For example:

    Original indexes:
    1000  1001  1005

    After normalization:
       0     1     5

The gap between the nodes is still the same.

So:

    1005 - 1000 + 1 = 6
    5 - 0 + 1 = 6

This keeps the indexes small and avoids unnecessarily large integer calculations.

---

## Algorithm

1. If the tree is empty, return `0`.

2. Create a queue containing:
   - the node
   - its position/index

   Start with:

       (root, 0)

3. While the queue is not empty:
   - Get the number of nodes in the current level.
   - Take the index of the first node as `minn`.
   - Process all nodes of this level.

4. For every node:
   - Normalize its index:

         curr_idx = curr_idx - minn

   - The first node's index becomes `first`.
   - The last node's index becomes `last`.

5. Add the children to the queue using their normalized index:

       left  = 2 * curr_idx + 1
       right = 2 * curr_idx + 2

6. After processing the level, calculate:

       width = last - first + 1

7. Keep the maximum width found.

8. Return the maximum width.

---

## Key Point

We are **not adding null nodes to the queue**.

Instead, their positions are automatically represented by the indexes.

So this:

        4   null   null   5

is represented by:

        3   .      .      6

and:

    6 - 3 + 1 = 4

That's the main trick behind the problem.

## Complexity

- **Time:** `O(n)` — every node is processed once.
- **Space:** `O(n)` in the worst case for the BFS queue.