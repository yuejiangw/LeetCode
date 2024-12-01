# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def traverse(root, targetSum):
            if not root.left and not root.right and sum(path) == targetSum:
                res.append(path[:]) # 一定要传副本
                return
            if not root.left and not root.right:
                return
            if root.left:
                path.append(root.left.val)
                traverse(root.left, targetSum)
                path.pop()
            if root.right:
                path.append(root.right.val)
                traverse(root.right, targetSum)
                path.pop()
            return

        if not root:
            return res
        path.append(root.val)
        traverse(root, targetSum)
        return res
            
class Solution:
    # 优化：不用每次都计算 sum，而是作为参数一起进行回溯
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        path = [root.val]
        res = []

        def traversal(root, target):
            if root.left == None and root.right == None:
                if target == 0:
                    res.append(path[:])
                return
            if root.left:
                path.append(root.left.val)
                traversal(root.left, target - root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                traversal(root.right, target - root.right.val)
                path.pop()
        
        traversal(root, targetSum - root.val)
        return res