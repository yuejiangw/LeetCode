# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # T: O(N)
        # S: O(N)
        def traverse(root, sum):
            if not root:
                return 0
            sum = sum * 2 + root.val
            if not root.left and not root.right:
                return sum
            return traverse(root.left, sum) + traverse(root.right, sum)
        
        return traverse(root, 0)