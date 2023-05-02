# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        counter = 0
        while curr != None:
            curr = curr.next
            counter += 1

        curr = head
        i = 0
        counter = counter // 2
        while i < counter:
            curr = curr.next
            i += 1

        return curr
