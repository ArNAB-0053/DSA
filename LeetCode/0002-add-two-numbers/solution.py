# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # creating a dummy linked list
        # initializing with 0
        dummy = ListNode(0)
        # curr points dummy's head
        curr = dummy

        # t1 and t2 points l1 and l2 repectively
        t1 = l1
        t2 = l2

        carry = 0
        while t1 or t2:
            summ = carry
            if t1:
                # summ = carry + t1
                summ += t1.val
            if t2:
                # summ = carry + t1(if t1) + t2
                summ += t2.val
            
            digit = summ % 10 # unit digit
            carry = summ // 10

            # create a new node with digit as val
            newNode = ListNode(digit)
            # store in the dummy
            # point newNode as next node
            curr.next = newNode
            # go to next node means now node
            curr = curr.next

            # go to next node of l1 and l2 if they exists
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next

        # still if carry exists
        if carry:
            # create a new node with carry as val
            newNode = ListNode(carry)
            # store it into dummy
            curr.next = newNode
            curr = curr.next
        
        # as added a dummy node 0
        # so skipping the first element
        return dummy.next