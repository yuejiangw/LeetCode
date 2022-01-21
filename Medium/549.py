# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        res = 0

        def dfs(root):
            # 返回一个二元组，分别表示由下至上到当前节点最大的升、降路径长度
            nonlocal res
            if not root:
                return 0, 0

            # 计算左右子树的递增/递减序列长度
            left_inc, left_dec = dfs(root.left)
            right_inc, right_dec = dfs(root.right)
            root_inc, root_dec = 1, 1

            if root.left:
                if root.left.val - 1 == root.val:
                    root_inc += left_inc
                elif root.left.val + 1 == root.val:
                    root_dec += left_dec

            if root.right:
                if root.right.val - 1 == root.val:
                    root_inc = max(root_inc, right_inc + 1)
                elif root.right.val + 1 == root.val:
                    root_dec = max(root_dec, right_dec + 1)
            # 左右序列都算了 root，因此最后要减1
            res = max(res, root_inc + root_dec - 1)
            return root_inc, root_dec

        dfs(root)
        return res
