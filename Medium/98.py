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

    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(root, min_node, max_node):
            if not root:
                return True
            if min_node and root.val <= min_node.val:
                return False
            if max_node and root.val >= max_node.val:
                return False
            return is_valid(root.left, min_node, root) \
                    and is_valid(root.right, root, max_node) 
        
        return is_valid(root, None, None)