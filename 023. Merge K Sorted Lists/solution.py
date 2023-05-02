# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for idx in range(len(lists)):
            while lists[idx] != None:
                res.append(lists[idx].val)
                lists[idx] = lists[idx].next
        head = ListNode()
        curr = head
        res.sort()
        for i in range(len(res)):
            temp = ListNode(res[i])
            curr.next = temp
            curr = curr.next
        return head.next
