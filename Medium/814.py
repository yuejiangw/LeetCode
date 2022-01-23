# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # 递归
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        # 后序遍历，如果当前叶子节点是值0，则直接剪掉
        if root.val == 0 and not root.left and not root.right:
            return None
        return root
