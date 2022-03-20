# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # T: O(N)
        # S: O(N)
        self.is_balance = True

        def get_height(root):
            if not root:
                return 0
            left = get_height(root.left)
            right = get_height(root.right)
            if abs(left - right) > 1:
                self.is_balance = False
            return max(left, right) + 1
        
        get_height(root)
        return self.is_balance