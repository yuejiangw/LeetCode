# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        return max(self.getHeight(root.left) + 1, self.getHeight(root.right) + 1)

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)