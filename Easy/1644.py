# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        def dfs(root, p, q):
            if not root:
                return False

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if not (left or right):
                return root == p or root == q
            
            if left and right:
                self.res = root
                return True

            if root == p or root == q:
                self.res = root
            return True
        
        dfs(root, p, q)
        return self.res