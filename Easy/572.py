# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 and node2:
                return False
            elif not node2 and node1:
                return False
            elif node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)
        
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        
        # 要么这两个树相等
        # 要么这个树是左树的子树
        # 要么这个树hi右树的子树
        return check(root, subRoot) \
               or self.isSubtree(root.left, subRoot) \
               or self.isSubtree(root.right, subRoot)