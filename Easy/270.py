# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # T: O(logN), S: O(1)
        closest = root.val
        while root:
            if abs(root.val - target) < abs(closest - target) or \
                (abs(root.val - target) == abs(closest - target) and root.val < closest):
                closest = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """ T: O(N), S: O(N) """
        min_diff = float('inf')
        nodes = {}

        def traverse(root, target):
            """ 直接遍历整棵树，并记录每个节点与 target 的差值 """
            nonlocal min_diff, nodes
            if not root:
                return
            diff = abs(root.val - target)
            nodes[diff] = root.val
            min_diff = min(min_diff, diff)
            traverse(root.left, target)
            traverse(root.right, target)

        traverse(root, target)
        return nodes[min_diff]

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """ T: O(logN), S: O(1) """
        res = root.val

        def traverse(root, target):
            """ 利用 bst 的性质二分搜索 """
            nonlocal res
            if not root:
                return
            if abs(res - target) > abs(root.val - target):
                res = root.val
            if root.val < target:
                traverse(root.right, target)
            elif root.val > target:
                traverse(root.left, target)

        traverse(root, target)
        return res
