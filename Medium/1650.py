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
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """ 相当于相交链表的思路 """
        p1, p2 = p, q
        while p1 != p2:
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q
            if p2.parent:
                p2 = p2.parent
            else:
                p2 = p
        return p1
