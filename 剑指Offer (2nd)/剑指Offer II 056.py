# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        # T: O(N)
        # S: O(N)
        values = set()

        def traverse(root):
            if not root:
                return False
            if k - root.val in values:
                return True
            values.add(root.val)
            return traverse(root.left) or traverse(root.right)
        
        return traverse(root)