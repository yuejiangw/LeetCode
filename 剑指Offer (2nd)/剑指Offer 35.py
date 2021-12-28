"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """ HashMap """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        curr = head
        hash_map = {}
        while curr:
            hash_map[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            hash_map[curr].next = hash_map.get(curr.next)
            hash_map[curr].random = hash_map.get(curr.random)
            curr = curr.next

        return hash_map[head]


class Solution:
    """ inplace operation """
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        # Copy each Node and link the copy node right behind the corresponding node.
        # For example, 1 → 2 → 3 would become 1 → 1' → 2 → 2' → 3 → 3'
        node, node_copy = head, None
        while node:
            node_copy = Node(node.val)
            node_copy.next = node.next
            node.next = node_copy
            node = node_copy.next
        # link the copy node's random pointer
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
        # divide the original node and the copied node into two linked lists,
        # return the second one
        new_head = head.next
        node, tmp = head, None
        while node and node.next:
            tmp = node.next
            node.next = tmp.next
            node = tmp

        return new_head
