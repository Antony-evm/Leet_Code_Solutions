# Given the roots of two binary trees root and subRoot,
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
# The tree tree could also be considered as a subtree of itself.


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.right, subRoot) or self.isSubtree(
                root.left, subRoot
            )

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left)
        return False
