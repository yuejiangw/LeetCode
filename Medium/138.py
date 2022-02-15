"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """ 借助哈希表存储老节点和新节点之间的映射关系, T: O(N), S: O(N) """
        new_head = Node(0)
        node_map = {}
        p1, p2 = head, new_head
        while p1:
            p2.next = Node(p1.val)
            p2 = p2.next
            node_map[p1] = p2
            p1 = p1.next
        p1 = head
        while p1:
            random_node = p1.random
            if random_node:
                node_map[p1].random = node_map[random_node]
            p1 = p1.next
        return new_head.next
