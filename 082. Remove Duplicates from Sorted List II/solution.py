# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        h = ListNode()
        t = h
        curr = head
        val = -101
        while curr.next:
            if curr.next.val!=curr.val:
                t.next = ListNode(curr.val)
                t = t.next
                curr = curr.next

            else:
                val = curr.val
                while curr.next:
                    if curr.val==val:
                        curr=curr.next
                    else:
                        break

        if curr.val != val:
            t.next = ListNode(curr.val)
        return h.next