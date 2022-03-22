# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # T: O(N)
        # S: O(N)
        self.res = float('-inf')

        def getMinMax(root):
            if not root:
                return (float('inf'), float('-inf'))
            left_min_max = getMinMax(root.left)
            right_min_max = getMinMax(root.right)
            # 以 root 为根的这棵树的最大值和最小值可以通过左右子树的最大最小值求出来
            root_min = min(root.val, left_min_max[0], right_min_max[0])
            root_max = max(root.val, left_min_max[1], right_min_max[1])
            # 在后序遍历的位置判断所有差值的最大最小值
            self.res = max(self.res, root.val - root_min, root_max - root.val)
            return (root_min, root_max)
        
        getMinMax(root)
        return self.res