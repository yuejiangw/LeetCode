# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        path = []
        res = ''

        def traversal(root):
            nonlocal res
            if not root:
                return
            path.append(chr(ord('a') + root.val))
            if not root.left and not root.right:
                tmp = ''.join(path)[::-1]
                if res == '':
                    res = tmp
                else:
                    res = min(res, tmp)
            traversal(root.left)
            traversal(root.right)
            path.pop()
        
        traversal(root)
        return res
