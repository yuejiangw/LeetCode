# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        """ 后序遍历 """

        if not root:
            return 0
        res = 0

        def is_unival(root):
            nonlocal res
            if not root:
                return True
            if not root.left and not root.right:
                res += 1
                return True

            left = is_unival(root.left)
            right = is_unival(root.right)

            if left and right:
                if not root.left or (root.left and root.left.val == root.val):
                    if not root.right or (root.right and root.right.val == root.val):
                        res += 1
                        return True
            return False

        is_unival(root)
        return res
