# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lca(self, root, p, q):
        if not root or root == p or root == q:
            return root
        l = self.lca(root.left, p, q)
        r = self.lca(root.right, p, q)
        if l and r:
            return root
        else:
            return l if not r else r

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        题目关键是在于如何判断 p 或 q 是否存在于树中，当我们找到其中一个节点时，我们需要判断另一个节点是否存在于以该节点为根的子树中
        具体做法是在找到 p 或 q 时，再次调用 lca 函数，如果返回的结果是另一个节点，说明另一个节点存在于以该节点为根的子树中
        '''
        res = self.lca(root, p, q)
        if res == p:
            if not self.lca(p, q, q):
                return None
        if res == q:
            if not self.lca(q, p, p):
                return None
        return res