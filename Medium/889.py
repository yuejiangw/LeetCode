# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        # 如果仅剩一个节点，则返回
        if len(preorder) == 1:
            return root
        # 前序遍历中根节点后面紧挨着的第一个元素就是左子树的根节点
        # 在后序遍历中根据左子树的根节点可以确定左子树的范围
        left_val = preorder[1]
        left_len = postorder.index(left_val) + 1
        left_pre = preorder[1: 1 + left_len]
        right_pre = preorder[1 + left_len:]

        # 在后序遍历中夹在左子树和根节点中间的范围就是右子树范围
        left_post = postorder[:left_len]
        right_post = postorder[left_len: -1]

        # 递归构造左右子树
        root.left = self.constructFromPrePost(left_pre, left_post)
        root.right = self.constructFromPrePost(right_pre, right_post)

        return root
