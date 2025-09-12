# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        path = defaultdict(int)
        odd = set()
        res = 0

        def adjustOdd(path, odd, val):
            if path[val] % 2 == 1:
                odd.add(val)
            elif path[val] % 2 == 0 and val in odd:
                odd.remove(val)

        def dfs(root):
            nonlocal res
            if not root:
                return
            path[root.val] += 1
            adjustOdd(path, odd, root.val)
            if len(odd) <= 1 and not root.left and not root.right:
                res += 1
            dfs(root.left)
            dfs(root.right)
            path[root.val] -= 1
            adjustOdd(path, odd, root.val)
        
        dfs(root)
        return res