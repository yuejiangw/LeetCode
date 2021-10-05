# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        nums = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            nums.append(root.val)
            traversal(root.right)
        traversal(root)
        counts = Counter(nums)
        mode_num = max(counts.values())
        res = []
        for k in counts.keys():
            if counts[k] == mode_num:
                res.append(k)
        return res