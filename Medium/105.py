# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def traverse(preorder, inorder):
            if len(preorder) == 0:
                return None
            
            root_val = preorder[0]
            root = TreeNode(root_val)

            # 切割中序遍历数组
            root_index = inorder.index(root_val)
            left_inorder = inorder[: root_index]
            right_inorder = inorder[root_index + 1:]

            # 根据中序切割结果切割前序遍历数组
            left_length = len(left_inorder)
            right_length = len(right_inorder)
            left_preorder = preorder[1: 1 + left_length]
            right_preorder = preorder[left_length + 1:]

            # 递归
            root.left = traverse(left_preorder, left_inorder)
            root.right = traverse(right_preorder, right_inorder)

            return root

        if len(preorder) == 0 or len(inorder) == 0:
            return None
        return traverse(preorder, inorder)