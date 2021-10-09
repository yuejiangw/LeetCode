# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def traversal(root, p, q):
            if (root.val >= p.val and root.val <= q.val)\
                or (root.val >= q.val and root.val <= p.val):
                return root
            else:
                if root.val < p.val and root.val < q.val:
                    return traversal(root.right, p, q)
                if root.val > p.val and root.val > q.val:
                    return traversal(root.left, p, q)
        
        return traversal(root, p, q)