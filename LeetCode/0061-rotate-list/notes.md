### Intuition

- convert it a circullar linkedlist
- remember the head (original head) 
- from original head go to `n-k-1` (n lenth of linkedlist) and break the next node
- store the new head that will be `tail.next`
- and tail.next will be `None`

> `n-k-1` -> -1 because we want to reach one node before the the new head
> then only we can do `newhead = tail.next` and `tail.next = None`

### edge cases
- n can be bigger than k so we need k %= n 
- if not head or not head.next return head
> e.g.: 
> k = 4, n = 3
> k %= n -> k = 1 -> means one rotation and 4 rotation is same

### Complexity
- Time Complexity: `O(n)`
- Space Complexity: `O(1)`