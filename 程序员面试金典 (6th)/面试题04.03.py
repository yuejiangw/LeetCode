# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from collections import deque
from typing import List


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        # n = number of tree nodes
        # T: O(n)
        # S: O(n)
        if not tree:
            return []
        res = []
        queue = deque([tree])
        while queue:
            length = len(queue)
            dummy_head = ListNode()
            curr = dummy_head
            for _ in range(length):
                node = queue.popleft()
                curr.next = ListNode(node.val)
                curr = curr.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(dummy_head.next)
        return res

