# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = set()
        curr = head
        while curr != None:
            d.add(curr.val)
            if curr.next and curr.next.val in d:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
