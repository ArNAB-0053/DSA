### Idea

A single binary search cannot find both the first and last occurrence in O(log n).

Reason:
- After finding the target, we cannot determine whether more occurrences exist on the left, right, both, or neither.
- Exploring both halves turns the algorithm into O(n) in the worst case.

Instead, perform two independent binary searches:

1. First occurrence
   - On nums[mid] == target:
       - Save the answer.
       - Continue searching LEFT (high = mid - 1).

2. Last occurrence
   - On nums[mid] == target:
       - Save the answer.
       - Continue searching RIGHT (low = mid + 1).


Time: O(log n) + O(log n) = O(log n)

Space: O(1)