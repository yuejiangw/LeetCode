# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        res = []

        def traverse(root):
            # 处理当前节点
            path.append(str(root.val))
            # 到达叶子节点时候收集结果
            if not root.left and not root.right:
                res.append('->'.join(path))
                return
            # 处理左右子树 + 回溯
            if root.left:
                traverse(root.left)
                path.pop()
            if root.right:
                traverse(root.right)
                path.pop()

        traverse(root)
        return res
            