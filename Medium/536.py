# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                i += 1
            elif s[i] == '-':
                start = i
                i += 1
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start: i])
                stack.append(TreeNode(num))
            elif s[i].isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                num = int(s[start: i])
                stack.append(TreeNode(num))
            elif s[i] == ')':
                node = stack.pop()
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                i += 1
        return stack[0]
