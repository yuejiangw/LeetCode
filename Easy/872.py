# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # T: O(N)
        # S: O(N)
        def get_height(root, leaf):
            if not root:
                return 0
            left = get_height(root.left, leaf)
            right = get_height(root.right, leaf)
            height = max(left, right) + 1
            if height == 1:
                leaf.append(root.val)
            return height
        
        leaf1, leaf2 = [], []
        get_height(root1, leaf1)
        get_height(root2, leaf2)
        return leaf1 == leaf2