# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict
from typing import List


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        '''
        难点在于二叉树不是一个单向结构，需要考虑向下搜索子树节点和向上搜索父节点
        解决这类问题一般有两个步骤：
        1. 将树转换为图
        2.BFS

        T: O(N), S: O(N)
        '''
        graph = defaultdict(list)

        def build_graph(node, parent):
            if not node:
                return
            if parent:
                # 建立 node - parent 的双向关系
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            # 递归处理左右子树
            build_graph(node.left, node)
            build_graph(node.right, node)

        build_graph(root, None)

        # BFS
        queue = deque([target.val])
        visited = set([target.val])
        distance = 0
        while queue:
            if distance == k:
                return list(queue)
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                for adj in graph[node]:
                    if adj not in visited:
                        visited.add(adj)
                        queue.append(adj)
            distance += 1
        
        return []