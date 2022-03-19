# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        # T: O(N)
        # S: O(N)
        res = []
        def traverse(root):
            if not root:
                return
            if root.left and not root.right:
                res.append(root.left.val)
            if root.right and not root.left:
                res.append(root.right.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        return res