# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def singleTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        return root.val + self.singleTilt(root.left) + self.singleTilt(root.right)
        
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        return abs(self.singleTilt(root.left) - self.singleTilt(root.right)) + \
            self.findTilt(root.left) + self.findTilt(root.right)