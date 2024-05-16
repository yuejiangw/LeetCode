# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        remain = targetSum - root.val
        if root.left is None and root.right is None:
            return remain == 0
        return self.hasPathSum(root.left, remain) or \
               self.hasPathSum(root.right, remain)

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traversal(root, target):
            # 当遇到叶子节点且 target 满足时候返回 true
            if root.left == None and root.right == None:
                return target == 0
            # DFS + 回溯
            if root.left:
                target -= root.left.val
                if traversal(root.left, target):
                    return True
                target += root.left.val
            if root.right:
                target -= root.right.val
                if traversal(root.right, target):
                    return True
                target += root.right.val
            return False

        if not root:
            return False
        return traversal(root, targetSum - root.val)
        