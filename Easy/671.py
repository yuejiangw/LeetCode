# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return -1
        # 由树的定义可知，根节点一定是整个树中最小的值，
        # 左右子节点中不同于 root.val 的那个值可能是第二小的值
        left = root.left.val
        right = root.right.val
        # 如果左右子节点都等于 root.val，则去左右子树递归寻找第二小的值
        if left == root.val:
           left = self.findSecondMinimumValue(root.left)
        if right == root.val:
            right = self.findSecondMinimumValue(root.right)

        if left == -1:
            return right
        if right == -1:
            return left
        # 如果左右子树都找到一个第二小的值，则返回更小的那一个
        return min(left, right)
