# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        inorder = sorted(preorder)

        def recover(preorder, inorder) -> TreeNode:
            if not preorder:
                return None

            root_val = preorder[0]
            root_idx = inorder.index(root_val)
            root = TreeNode(root_val)

            left_in = inorder[:root_idx]
            right_in = inorder[root_idx+1:]

            left_pre = preorder[1:1+len(left_in)]
            right_pre = preorder[1+len(left_in):]

            root.left = recover(left_pre, left_in)
            root.right = recover(right_pre, right_in)
            return root

        return recover(preorder, inorder)
