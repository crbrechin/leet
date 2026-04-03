# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: # Handle empty case
            return None

        c = head # Current node

        while c and c.next:
            # print(c.val) # DEBUG
            if c.val == c.next.val:
                c.next = c.next.next
            else:
                c = c.next
        return head
