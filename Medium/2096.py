# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        分别记录从根节点到 startValue 和 destValue 的路径
        去除上述两个路径的公共前缀
        最后将 startPath 全部变成 U 和 destPath 接在一起
        """   
        # T: O(N)
        # S: O(N)
        path = []
        startPath = ''
        destPath = ''

        def traverse(root: TreeNode):
            nonlocal startPath, destPath
            if not root:
                return
            if root.val == startValue:
                startPath = ''.join(path)
            elif root.val == destValue:
                destPath = ''.join(path)
            # 二叉树遍历
            path.append('L')
            traverse(root.left)
            path.pop()

            path.append('R')
            traverse(root.right)
            path.pop()
        
        # 寻找走到 startValue 和 destValue 的方向路径
        traverse(root)
        # 去除公共前缀
        i = 0
        while i < len(startPath) \
            and i < len(destPath) and startPath[i] == destPath[i]:
                i += 1
        startPath, destPath = startPath[i:], destPath[i:]
        
        # 将走向 startValue 的方向路径全部变为 U
        # 之后与 destPath 拼接
        return 'U' * len(startPath) + destPath

