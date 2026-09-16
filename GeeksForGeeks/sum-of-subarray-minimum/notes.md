## Approach

The main problem is that we need to find the minimum of **every possible subarray** and add them all.

Doing this directly would take `O(n²)` or worse.

Instead of looking at every subarray, we can look at the problem from the other side:

> **For every element, find how many subarrays have this element as their minimum.**

Then we can calculate its **contribution** to the final answer.

### Why Contribution?

Suppose:

```text
arr = [3, 1, 2]
```

For the element `1`, there are several subarrays where `1` is the minimum:

```text
[1]
[3, 1]
[1, 2]
[3, 1, 2]
```

So `1` contributes:

```text
1 × 4 = 4
```

Instead of calculating the minimum of each subarray separately, we calculate:

```text
contribution = value × number of subarrays where it is the minimum
```

We do this for every element and add all the contributions.

---

## How do we find the number of subarrays?

For every `arr[i]`, we need to know how far we can extend:

* to the **left**
* to the **right**

while `arr[i]` can still be considered the minimum.

For this we find:

### Previous Equal or Smaller Element (PESE)

Find the first element on the left which is **smaller or equal** to `arr[i]`.

```text
PESE[i]
```

The number of choices on the left is:

```text
left = i - PESE[i]
```

### Next Smaller Element (NSE)

Find the first element on the right which is **strictly smaller** than `arr[i]`.

```text
NSE[i]
```

The number of choices on the right is:

```text
right = NSE[i] - i
```

---

## Why multiply `left × right`?

For every possible starting position on the left, we can combine it with every possible ending position on the right.

So:

```text
number of subarrays = left × right
```

Therefore:

```text
contribution = arr[i] × left × right
```

or:

```text
contribution = arr[i] × (i - PESE[i]) × (NSE[i] - i)
```

Then:

```text
answer = sum of contribution of every element
```

---

## Why `>` on one side and `>=` on the other?

When there are equal values, we don't want both of them to count the same subarray.

So we handle equal values from only one side.

```python
# PESE
while stack and arr[stack[-1]] > arr[i]:
    stack.pop()
```

Here, an equal value is allowed to stay.

```python
# NSE
while stack and arr[stack[-1]] >= arr[i]:
    stack.pop()
```

Here, an equal value is removed.

This gives us a fixed rule for which equal element gets to count a subarray.

---

## Complexity

We calculate PESE and NSE using monotonic stacks.

Each element is pushed and popped at most once.

Therefore:

```text
Time:  O(n)
Space: O(n)
```
