# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        pre = 0

        def traversal(root):
            nonlocal pre
            if not root:
                return
            traversal(root.right)
            root.val += pre
            pre = root.val
            traversal(root.left)
        traversal(root)
        return root
