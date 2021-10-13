# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        def get_depth(root):
            nonlocal res
            if not root:
                return 0
            left_depth = get_depth(root.left)
            right_depth = get_depth(root.right)
            res = max(res, left_depth + right_depth)
            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return res