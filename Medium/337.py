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

    def rob(self, root: TreeNode) -> int:
        """记忆化递归"""
        dp = dict()
        def rob_tree(node):
            if not node:
                return 0
            # 记忆化递归
            if node in dp.keys():
                return dp[node]
            # 偷
            res1 = 0
            if node.left is not None:
                res1 += (rob_tree(node.left.left) + rob_tree(node.left.right))
            if node.right is not None:
                res1 += (rob_tree(node.right.left) + rob_tree(node.right.right))
            res1 += node.val
            # 不偷
            res2 = rob_tree(node.left) + rob_tree(node.right)

            dp[node] = max(res1, res2)
            return dp[node]
        return rob_tree(root)