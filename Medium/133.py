"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = deque([node])
        # use a map to store the copied nodes
        graph = {}
        graph[node.val] = Node(node.val)
        # use bfs to expand the nodes from level to level
        while queue:
            length = len(queue)
            for _ in range(length):
                n = queue.popleft()
                adj = n.neighbors
                # generate n's neighbor nodes
                for neighbor in adj:
                    # if not expanded the node, then add it to queue and generate a copy of it in map
                    if neighbor.val not in graph:
                        queue.append(neighbor)
                        graph[neighbor.val] = Node(neighbor.val)
                    # link the copies in the map with each other
                    if graph[n.val].neighbors is None:
                        graph[n.val].neighbors = []
                    graph[n.val].neighbors.append(graph[neighbor.val])
        return graph[node.val]
