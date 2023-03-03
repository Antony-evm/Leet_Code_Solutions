Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next==None:
            return head
        
        curr = head
        while True:
            curr.val,curr.next.val = curr.next.val,curr.val
            curr = curr.next.next
            if curr== None or curr.next==None:
                break
        return head