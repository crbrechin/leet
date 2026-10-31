# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        i = -1
        nodes = []
        while head:
            i += 1
            n = head
            nodes.append(n)
            head = head.next
                
        return nodes[ceil(i/2)]
