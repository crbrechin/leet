# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0) # Dummy
        l3 = d # Output list
        c = 0 # Carry
        while(l1 or l2 or c):
            # print(f'{l1.val + l2.val}') # DEBUG
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            t = (a + b + c) # Total
            c = t // 10 # Get the carry
            t = t % 10 # Get the remainder
            # print(f'{c}, {t}')

            l3.next = ListNode(t)
            l3 = l3.next

            # Move to the next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

            print(l3.val) #DEBUG
        print(l3)
        d = d.next
        return d
