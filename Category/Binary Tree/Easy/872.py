# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traversal(root, res):
            # 左 - 根 - 右，中序遍历
            if not root:
                return
            traversal(root.left, res)
            if not root.left and not root.right:
                res.append(root.val)
            traversal(root.right, res)
        
        res1, res2 = [], []
        traversal(root1, res1)
        traversal(root2, res2)
        return res1 == res2