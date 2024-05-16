# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            res += root.left.val
        return res + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
    
# 另一种写法, 借助全局变量来更新结果
class Solution:
    res = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if not root:
                return
            # 遇到左叶子时收集结果
            if root.left and root.left.left == None and root.left.right == None:
                self.res += root.left.val
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        return self.res