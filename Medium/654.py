# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        def traverse(nums):
            # 递归终止条件：无法分割
            if len(nums) == 0:
                return None
            
            # 选取最大值构造根节点
            root_val = max(nums)
            root = TreeNode(root_val)
            
            # 分割左右子树的元素集合
            root_idx = nums.index(root_val)
            prefix = nums[: root_idx]
            suffix = nums[root_idx + 1:]

            # 构造左右子树
            root.left = traverse(prefix)
            root.right = traverse(suffix)
            return root
        
        return traverse(nums)