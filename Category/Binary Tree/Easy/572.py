# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(p, q):
            if not p and not q:
                return True
            elif p and not q:
                return False
            elif q and not p:
                return False
            elif p.val != q.val:
                return False
            return compare(p.left, q.left) and compare(p.right, q.right)
        
        def traverse(root, subRoot):
            # subRoot 不存在但 root 还存在的时候要返回 True
            if root and not subRoot:
                return True
            elif subRoot and not root:
                return False
            elif not root and not subRoot:
                return True
            return compare(root, subRoot) or traverse(root.left, subRoot) or traverse(root.right, subRoot) 
        
        return traverse(root, subRoot)
