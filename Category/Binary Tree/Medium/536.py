# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(s):
            if s[i] != '(' and s[i] != ')':
                j = i + 1
                while j < len(s) and s[j] != '(' and s[j] != ')':
                    j += 1
                num = int(s[i: j])
                stack.append(TreeNode(num))
                i = j
            elif s[i] == '(':
                i += 1
            elif s[i] == ')':
                node = stack.pop()
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                i += 1
        return stack[0] if stack else None
