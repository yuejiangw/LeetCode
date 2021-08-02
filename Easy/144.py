# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """前序遍历：中，左，右"""
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归版本
        def recursion(root):
            if not root:
                return
            res.append(root.val)
            recursion(root.left)
            recursion(root.right) 
        res = []
        recursion(root)
        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 非递归版本（迭代）
        if not root:
            return []
        res = []
        stack = [root]
        while stack != []:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res