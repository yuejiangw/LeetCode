# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_bst(self, root):
        """ 判断一棵树是不是 BST """
        def traverse(root: TreeNode, min: TreeNode, max: TreeNode) -> bool:
            if not root:
                return True
            if min and min.val >= root.val:
                return False
            if max and max.val <= root.val:
                return False
            return traverse(root.left, min, root) and traverse(root.right, root, max)
        return traverse(root, None, None)

    def get_count(self, root):
        """ 统计树中节点的数量 """
        if not root:
            return 0
        return 1 + self.get_count(root.left) + self.get_count(root.right)

    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if self.is_bst(root):
            return self.get_count(root)
        l = self.largestBSTSubtree(root.left)
        r = self.largestBSTSubtree(root.right)
        return max(l, r)
