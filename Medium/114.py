# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 后序遍历
        if not root:
            return 
        self.flatten(root.left)
        self.flatten(root.right)
        
        right_tree = root.right
        root.right = root.left
        root.left = None
        # 找到左子树中最右叶子，将root.right挂在它的右子树上
        while root.right != None:
            root = root.right
        root.right = right_tree
