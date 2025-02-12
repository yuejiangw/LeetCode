# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import deque, defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        层序遍历 + 局部排序
        k = width of the tree, N = number of nodes in the tree
        T: O(Nlog(N/k))
        S: O(N)
        '''
        res = []
        if not root:
            return res
        col_2_values = defaultdict(list)
        min_col, max_col = float('inf'), float('-inf')
        queue = deque()
        queue.append([root, 0, 0])
        while queue:
            node, row, col = queue.popleft()
            col_2_values[col].append((row, node.val))
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if node.left:
                queue.append([node.left, row + 1, col - 1])
            if node.right:
                queue.append([node.right, row + 1, col + 1])
        for c in range(min_col, max_col + 1):
            res.append([item[1] for item in sorted(col_2_values[c])])
        return res


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
