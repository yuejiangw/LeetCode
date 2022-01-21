"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # 右子树的最小值就是 successor
        p = node.right
        while p and p.left:
            p = p.left
        if p:
            return p
        # 没有右子树的话，第一个比自己大的父节点就是 successor
        # p 可能是父节点的左子节点也可能是右子节点
        # 只有 p 是左子节点的时候父节点才是 successor，否则就继续向上搜索
        p = node
        while p.parent and p.parent.right == p:
            p = p.parent
        return p.parent
