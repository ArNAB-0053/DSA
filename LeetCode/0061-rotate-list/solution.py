# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Intuition: 
    # - convert it a circullar linkedlist
    # - remember the head (original head) 
    # - from original head go to `n-k-1` (n lenth of linkedlist) and break the next node
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # stores length of linkedlist
        n = 1

        # current node, which eventually works as tail node
        curr = head
        # counts lenth of linkedlist
        while curr.next:
            curr = curr.next
            n += 1

        # k can be bigger than n as well
        # and instead of doing repeated rotation
        # we can just keep k between n

        # e.g.
        # k = 4, n = 3
        # k %= n -> k = 1 -> means one rotation and 4 rotation is same
        k %= n

        # if then k comes as 0 means we don't need rotation anyway
        if k == 0:
            return head

        # converting to circular linkedlist
        # curr now is the tail node for original linkedlist
        curr.next = head

        # the new tail will be at position (n - k - 1)
        # n-k-1 -> -1 because we want to reach one node before the the new head,
        # then only we can do newhead = tail.next and tail.next = None
        steps = n - k - 1

        # the new tail
        tail = head

        # for upto steps to get before new node and to new tail
        for _ in range(steps):
            tail = tail.next
        
        # break the circular linkedlist, converting it to singly linkedlist again
        # and the new head will be tail.next 
        newHead = tail.next
        # and tail.next will be none
        tail.next = None
        return newHead
