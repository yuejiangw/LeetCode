# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def traversal(preorder, inorder):
            # finish recurrsion
            if len(preorder) == 0:
                return None

            # build root node
            root_val = preorder[0]
            root = TreeNode(root_val)

            # divide inorder traversal result
            root_pos = inorder.index(root_val)
            left_inorder = inorder[:root_pos]
            right_inorder = inorder[root_pos + 1:]

            # divide preorder traversal result
            left_preorder = preorder[1: 1 + len(left_inorder)]
            right_preorder = preorder[1 + len(left_inorder):]

            # recurrsion
            root.left = traversal(left_preorder, left_inorder)
            root.right = traversal(right_preorder, right_inorder)

            return root
        return traversal(preorder, inorder)