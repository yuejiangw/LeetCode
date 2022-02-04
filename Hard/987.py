# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        """
        先把各个节点的坐标输出，然后按照col排序，当col相同的时候按照row排序，
        当row相同的时候按照val排序，最后将节点序列拼接成vertical traversal的格式
        """
        nodes = []

        def traverse(root, row, col):
            if not root:
                return
            nodes.append([root.val, row, col])
            traverse(root.left, row + 1, col - 1)
            traverse(root.right, row + 1, col + 1)
        traverse(root, 0, 0)
        nodes = sorted(nodes, key=lambda x: (x[2], x[1], x[0]))
        res = []
        i = 0
        while i < len(nodes):
            tmp = [nodes[i][0]]
            j = i + 1
            while j < len(nodes) and nodes[j][2] == nodes[i][2]:
                tmp.append(nodes[j][0])
                j += 1
            i = j
            res.append(tmp)
        return res
