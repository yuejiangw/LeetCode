# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def maximumAverageSubtree(self, root: TreeNode) -> float:

        def traversal(root):
            # 后序遍历, 返回值是 (count, sum)
            if not root:
                return 0, 0

            left_count, left_sum = traversal(root.left)
            right_count, right_sum = traversal(root.right)

            root_count = left_count + right_count + 1
            root_sum = left_sum + right_sum + root.val

            self.res = max(self.res, root_sum / root_count)

            return root_count, root_sum
        
        traversal(root)
        return self.res