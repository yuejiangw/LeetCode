# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, root):
        if not root:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right:
            return root

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)

        if left_depth == right_depth:
            return root
        elif left_depth < right_depth:
            return self.lcaDeepestLeaves(root.right)
        else:
            return self.lcaDeepestLeaves(root.left)
