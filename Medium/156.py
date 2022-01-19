# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left:
            return root
        # 左子树 → 根
        # 根 → 右子树
        # 右子树 → 左子树
        l = root.left
        r = root.right
        res = self.upsideDownBinaryTree(root.left)
        root.left = None
        root.right = None
        l.left = r
        l.right = root
        return res
