# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp_smaller = ListNode()
        temp_bigger = ListNode()
        ptr1 = head_smaller = temp_smaller
        ptr2 = head_bigger = temp_bigger
        curr = head
        while curr:
            if curr.val<x:
                head_smaller.next = ListNode(curr.val)
                head_smaller = head_smaller.next
            else:
                head_bigger.next = ListNode(curr.val)
                head_bigger = head_bigger.next
            curr = curr.next
        head_smaller.next=ptr2.next
        return ptr1.next