# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# #
# The number of nodes in the list is n.
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        res, curr = [], head
        while curr != None:
            res.append(curr.val)
            curr = curr.next
        res[0:k] = res[k - 1 :: -1]
        counter = 2
        while k * counter <= len(res):
            res[k * (counter - 1) : k * counter] = res[k * counter - 1 : k * (counter - 1) - 1 : -1]
            counter += 1
        head = ListNode(res[0])
        curr = head
        for i in range(1, len(res)):
            curr.next = ListNode(res[i])
            curr = curr.next
        return head
