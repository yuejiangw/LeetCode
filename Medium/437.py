# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """ 双重递归，首先先序遍历每个节点，再以每个节点作为起始点递归寻找满足条件的路径 """
    res = 0

    def dfs(self, root, targetSum):
        if not root:
            return
        if root.val == targetSum:
            self.res += 1
        self.dfs(root.left, targetSum - root.val)
        self.dfs(root.right, targetSum - root.val)

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        self.dfs(root, targetSum)
        # 由于路径不需要从 root 开始，因此第二个参数为 targetSum，不是 targetSum - root.val
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.res
