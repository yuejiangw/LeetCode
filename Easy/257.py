# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def traverse(node, path, res):
            path.append(node.val)
            if node.left is None and node.right is None:
                res.append('->'.join([str(x) for x in path]))
                return
            if node.left is not None:
                traverse(node.left, path, res)
                path.pop()
            if node.right is not None:
                traverse(node.right, path, res)
                path.pop()
        path = []
        res = []
        if not root:
            return []
        traverse(root, path, res)
        return res
