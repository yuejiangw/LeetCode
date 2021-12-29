# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def traversal(root) -> int:
            if not root:
                return 0
            elif root.val >= low and root.val <= high:
                return root.val + traversal(root.left) + traversal(root.right)
            elif root.val < low:
                return traversal(root.right)
            elif root.val > high:
                return traversal(root.left)
        return traversal(root)
