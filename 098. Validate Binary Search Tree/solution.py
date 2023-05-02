# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left
# subtree
#  of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [(root, -float("inf"), float("inf"))]
        while len(stack):
            node, left, right = stack.pop()
            if node.val <= left or node.val >= right:
                return False
            if node.left:
                stack.append((node.left, left, node.val))
            if node.right:
                stack.append((node.right, node.val, right))
        return True
