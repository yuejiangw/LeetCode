from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2024-04-26
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代法，中左右遍历
        stack = deque()
        res = []
        while root or stack:
            # 如果已经走到了叶子节点，则处理右子树
            if not root:
                root = stack.pop().right
            res.append(root.val)
            # 如果有右子树，则当前节点要入栈以便后续处理
            if root.right:      
                stack.append(root)
            # 去左子树
            root = root.left
        return res

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