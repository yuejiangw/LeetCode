# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """非递归（迭代）版本实现"""
        if not root:
            return []
        res = []
        stack =[root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return res[::-1]

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """递归版本实现"""
        def recursion(root):
            if not root:
                return
            recursion(root.left)
            recursion(root.right)
            res.append(root.val)
        res = []
        recursion(root)
        return res