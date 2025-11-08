# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head # LinkedList
        c = 0 # Counter
        while h.next != None: # While we're not at the end of the list
            h = h.next # Move to the next node
            c += 1 # Increment counter
        
        # Get the halfway counter
        c = ceil(c / 2) # Round up
        while c > 0: # Walk through the list again
            head = head.next # Move through the list
            c -= 1 # Decrement the counter
        return head
