# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 返回一个长度为2的数组，下标0代表不偷，下标1代表偷
        def rob_tree(node):
            if not node:
                return [0, 0]
            # 后序遍历
            left = rob_tree(node.left)
            right = rob_tree(node.right)
            # 偷
            val1 = node.val + left[0] + right[0]
            # 不偷
            val2 = max(left) + max(right)
            return [val2, val1]
        
        return max(rob_tree(root))