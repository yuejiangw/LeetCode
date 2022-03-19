# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = float('inf')
    pre = None

    def minDiffInBST(self, root: TreeNode) -> int:
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.pre:
                self.res = min(self.res, root.val - self.pre.val)
            self.pre = root
            inorder(root.right)
        
        inorder(root)
        return self.res