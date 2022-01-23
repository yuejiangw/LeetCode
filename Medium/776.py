# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: TreeNode, target: int) -> List[TreeNode]:
        """
        输入一颗 BST 和一个 target，返回两棵 BST 的根节点，
        第一棵所有节点都小于等于 target，第二棵所有节点都大于 target
        """
        if not root:
            return [None, None]

        res = [None] * 2
        if root.val <= target:
            # root 必是第一棵 BST 的根节点
            res[0] = root
            # 第二棵 BST 的根节点需要去右子树算
            right = self.splitBST(root.right, target)
            res[1] = right[1]
            # 保证 root 的右子树都是小于 target 的
            root.right = right[0]
        else:
            # root 必是第二棵 BST 的根节点
            res[1] = root
            # 第一棵 BST 的根节点需要去左子树算
            left = self.splitBST(root.left, target)
            res[0] = left[0]
            # 保证 root 的左子树都是大于 target 的
            root.left = left[1]
        return res
