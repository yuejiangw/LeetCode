# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        path = []
        def inorder_traverse(root):
            if not root:
                return
            inorder_traverse(root.left)
            path.append(root.val)
            inorder_traverse(root.right)
        if not root:
            return True
        inorder_traverse(root)
        for i in range(1, len(path)):
            # 要用 <=，因为不能有重复元素
            if path[i] <= path[i - 1]:
                return False
        return True
