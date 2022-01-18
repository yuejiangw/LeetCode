# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """ Traverse, O(n) """
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        res = None

        def inorder(root):
            nonlocal res
            if not root or res:
                return
            inorder(root.left)
            if not res and root.val > p.val:
                res = root
            inorder(root.right)
        inorder(root)
        return res


class Solution:
    """ Binary Search, O(logN) """
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        successor = None

        def find_min(root):
            if not root:
                return None
            while root.left:
                root = root.left
            return root

        # binary search
        while root:
            if root.val < p.val:
                root = root.right
            elif root.val > p.val:
                # root.val > p.val时需要同时更新successor
                successor = root
                root = root.left
            else:
                # 如果有右子树，则返回右子树的最小值，否则返回当前子树根节点
                if root.right:
                    successor = find_min(root.right)
                break
        return successor
