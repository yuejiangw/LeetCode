# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getHeight(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return max(self.getHeight(root.left) + 1, self.getHeight(root.right) + 1)

    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        if abs(self.getHeight(root.right) - self.getHeight(root.left)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)