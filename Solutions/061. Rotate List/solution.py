# Given the head of a linked list, rotate the list to the right by k places.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1

        k = k % length
        curr.next = head

        temp = head
        for _ in range(length - k - 1):
            temp = temp.next

        answer = temp.next
        temp.next = None
        return answer
