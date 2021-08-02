# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(node1, node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None and node2 is not None:
                return False
            elif node1 is not None and node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        
        if not root:
            return True
        return check(root.left, root.right)