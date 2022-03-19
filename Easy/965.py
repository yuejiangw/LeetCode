# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre = None
    def isUnivalTree(self, root: TreeNode) -> bool:
        # T: O(N)
        # S: O(N)
        def traverse(root):
            if not root:
                return True
            if self.pre:
                if self.pre.val != root.val:
                    return False
            self.pre = root
            return traverse(root.left) and traverse(root.right)
        
        return traverse(root)