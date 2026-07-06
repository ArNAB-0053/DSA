# Intuition

### Step 1: Sort the intervals

Sort the intervals by:

* **start** in ascending order
* if two intervals have the same start, **end** in descending order

Example:

```python
[[1,2], [1,5], [2,6], [2,1], [3,4]]
```

becomes

```python
[[1,5], [1,2], [2,6], [2,1], [3,4]]
```

This ensures that when two intervals have the same start, the larger interval appears before the smaller one, allowing covered intervals to be detected correctly during traversal.

### Step 2: Initialize variables

* `max_end` stores the largest end value encountered so far.
* `covered` keeps track of the number of covered intervals.

Initialize:

```python
max_end = intervals[0][1]
covered = 0
```

### Step 3: Traverse the sorted intervals

For each interval:

* If `current_end <= max_end`, the current interval is covered by a previously processed interval, so increment `covered`.
* Otherwise, update `max_end` to `current_end`.

Since the intervals are sorted by start, a previous interval with `end >= current_end` covers the current interval.

### Result

The number of remaining intervals is:

```python
len(intervals) - covered
```
