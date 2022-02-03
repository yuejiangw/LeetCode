"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def dfs(head):
            last = head
            curr = head
            while curr:
                next_node = curr.next
                if curr.child:
                    # flatten the child nodes
                    child_last = dfs(curr.child)
                    next_node = curr.next

                    # link the flattened child to current node
                    curr.next = curr.child
                    curr.child.prev = curr

                    # link the falttened child to the next node
                    if next_node:
                        child_last.next = next_node
                        next_node.prev = child_last

                    # set current node's child to None
                    curr.child = None
                    last = child_last
                else:
                    last = curr
                curr = curr.next
            return last

        dfs(head)
        return head
