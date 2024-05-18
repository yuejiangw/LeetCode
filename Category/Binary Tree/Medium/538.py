# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traversal(curr):
            if not curr:
                return None
            traversal(curr.right)
            curr.val += self.pre
            self.pre = curr.val
            traversal(curr.left)
        self.pre = 0
        traversal(root)
        return root