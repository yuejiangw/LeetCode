# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        # T: O(N)
        # S: O(N)
        colors = set()

        def traverse(root):
            if not root:
                return
            colors.add(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return len(colors)