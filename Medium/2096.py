# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        res = []
        def get_path(root: TreeNode, target: int, path: List[int]):
            if not root:
                return
            if root.val == target:
                res.append(''.join(path))
                return

            # 搜左边
            path.append('L')
            get_path(root.left, target, path)
            path.pop()

            # 搜右边
            path.append('R')
            get_path(root.right, target, path)
            path.pop()
        
        get_path(root, startValue, [])
        get_path(root, destValue, [])
        p1, p2 = res[0], res[1]
        # 去除公共前缀
        i, m, n = 0, len(p1), len(p2)
        while i < m and i < n and p1[i] == p2[i]:
            i += 1
        # 将 startPath 的方向全部变为 U
        p1 = 'U' * (m - i)
        p2 = p2[i:]
        return p1 + p2
