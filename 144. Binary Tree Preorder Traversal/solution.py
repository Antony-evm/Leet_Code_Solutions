# Given the root of a binary tree, return the preorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        stack = [root]
        while stack:
            print(stack)
            curr = stack.pop(0)
            res.append(curr.val)
            if curr.right:
                stack.insert(0, curr.right)
            if curr.left:
                stack.insert(0, curr.left)
        return res
