# Given the root of a binary tree, return the postorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            stack = deque([root])
            res = []
            while stack:
                curr = stack.popleft()
                res.append(curr.val)
                if curr.left:
                    stack.appendleft(curr.left)
                if curr.right:
                    stack.appendleft(curr.right)

            return res[::-1]                
