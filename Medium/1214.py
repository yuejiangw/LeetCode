# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        # 对于 root1 上的每一个节点值v，在 root2 上利用 BST 性质搜索 target - v 是否存在
        # T: O(m * logn)
        # S: O(logm + logn)

        def find(root, target):
            if not root:
                return False
            if root.val == target:
                return True
            if root.val > target:
                return find(root.left, target)
            else:
                return find(root.right, target)

        res = False
        def traversal(root1, root2):
            nonlocal res
            if not root1:
                return
            if find(root2, target - root1.val):
                res = True
                return
            traversal(root1.left, root2)
            traversal(root1.right, root2)
        
        traversal(root1, root2)
        return res
