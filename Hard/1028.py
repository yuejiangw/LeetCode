# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import re


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        if not traversal:
            return None
        traversal = re.findall(r'\w+|-+', traversal)

        def dfs(traversal):
            if not traversal:
                return None
            root = TreeNode(int(traversal[0]))
            children = [[], []]
            idx = -1
            for i in traversal[1:]:
                if i == '-':
                    idx += 1
                elif i.isdigit():
                    children[idx].append(i)
                else:
                    children[idx].append(i[1:])
            root.left = dfs(children[0])
            root.right = dfs(children[1])
            return root
        return dfs(traversal)
