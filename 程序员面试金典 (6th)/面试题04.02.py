# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # T: O(N)
        # S: O(logN)

        def build(nums):
            if not nums:
                return None
            idx = len(nums) // 2
            root = TreeNode(nums[idx])
            root.left = build(nums[:idx])
            root.right = build(nums[idx + 1:])
            return root
        
        return build(nums)