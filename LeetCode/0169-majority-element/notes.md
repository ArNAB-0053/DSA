# Boyer-Moore Voting Algorithm

**TC:** `O(n)`
**SC:** `O(1)`

### Intuition

* Keep a `candidate` and a `count`.
* If `count` becomes `0`, choose the current number as the new candidate.
* If the current number matches the candidate, increase `count`.
* Otherwise, decrease `count`.

### This works here because :

* Every occurrence of a different element cancels out one occurrence of the current candidate.
* The majority element appears **more than `n/2` times**.
* Therefore, even after all possible cancellations, the majority element cannot be completely eliminated.
* The candidate remaining at the end is guaranteed to be the majority element.

> **Note:** can be done by using `dictionary` but that would take `O(n) time and space complexity`, where `Boyer-Moore Voting Algorithm` takes `O(n) time but O(1) space complexity`
