# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        d = ListNode(0, head) # Dummy
        p = d # Previous
        c = head # Current

        while c:
            if c.val == val:
                p.next = c.next # Skip
            else:
                p = c
            c = c.next # Move to the next

        return d.next
