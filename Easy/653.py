# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)

        def two_sum(nums, target):
            if not nums:
                return False
            i, j = 0, len(nums) - 1
            while i < j:
                summation = nums[i] + nums[j]
                if summation == target:
                    return True
                elif summation < target:
                    i += 1
                else:
                    j -= 1
            return False

        return two_sum(res, k)
