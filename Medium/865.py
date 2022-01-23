# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, root):
        if not root:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root.left and not root.right:
            return root
        # 获取 root 左右子树的最大深度
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        # 如果两边的深度相同，则说明当前 root 结点就是我们想要的结果
        if left_depth == right_depth:
            return root
        # 否则去较深的一侧继续寻找
        elif left_depth > right_depth:
            return self.subtreeWithAllDeepest(root.left)
        else:
            return self.subtreeWithAllDeepest(root.right)
