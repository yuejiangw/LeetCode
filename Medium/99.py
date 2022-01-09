# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    first = None
    secon = None
    pre = TreeNode(float('-inf'))
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root: return
            inorder(root.left)
            if not self.first and root.val < self.pre.val:
                self.first = self.pre
            if self.first and root.val < self.pre.val:
                self.second = root
            self.pre = root
            inorder(root.right)
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
