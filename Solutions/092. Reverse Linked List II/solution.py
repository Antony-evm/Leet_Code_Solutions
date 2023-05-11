# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
  
        l = []
        while head:
            l.append(head.val)
            head=head.next
        l[left-1:right] = l[left-1:right][::-1]
        head = None
        for i in l[::-1]:
            head = ListNode(i,head)
        return head

    
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseN(head, n):
            if n == 1:
                self.successor = head.next
                return head
            newHead = reverseN(head.next, n - 1)
            tail = head.next.next
            head.next.next = head
            head.next = tail

            return newHead

        if left == 1:
            return reverseN(head, right)
        head.next = self.reverseBetween(head.next, left -1, right -1)
        return head

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n1 = n2 = head
        prev = dummy = ListNode(0, head)

        for _ in range(left - 1):
            n1 = n1.next
            prev = prev.next

        for _ in range(right - 1):
            n2 = n2.next

        while n1 != n2:
            tmp = n1.next
            n1.next = n2.next
            n2.next = n1
            n1 = tmp
        prev.next = n2

        return dummy.next