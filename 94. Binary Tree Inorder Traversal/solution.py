# Given the root of a binary tree, return the inorder traversal of its nodes' values.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def traversal(root):
            if root == None:
                return

            traversal(root.left)
            result.append(root.val)
            traversal(root.right)

        traversal(root)
        return result