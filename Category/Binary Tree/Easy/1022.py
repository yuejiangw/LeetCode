# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 2025-09-14
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        path = 0
        res = 0

        def traversal(root):
            nonlocal path, res
            if not root:
                return
            path = path * 2 + root.val
            if not root.left and not root.right:
                res += path
            traversal(root.left)
            traversal(root.right)
            path = (path - root.val) // 2
        
        traversal(root)
        return res

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # T: O(N)
        # S: O(N)
        def traverse(root, sum):
            if not root:
                return 0
            sum = sum * 2 + root.val
            if not root.left and not root.right:
                return sum
            return traverse(root.left, sum) + traverse(root.right, sum)
        
        return traverse(root, 0)