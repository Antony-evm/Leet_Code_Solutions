# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [root]
        while stack:
            curr = stack.pop(0)
            if curr.left:
                stack.append(curr.left)
                if curr.left.left == None and curr.left.right == None:
                    res += curr.left.val
            if curr.right:
                stack.append(curr.right)

        return res
