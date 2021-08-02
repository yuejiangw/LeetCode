# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        if not root:
            return True
        elif abs(get_height(root.left) - get_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)