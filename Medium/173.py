# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class BSTIterator:
    # T: O(1), S: O(h)
    def __init__(self, root: TreeNode):
        self.stack = deque()
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        tmp = self.stack.pop()
        res = tmp.val
        tmp = tmp.right
        while tmp:
            self.stack.append(tmp)
            tmp = tmp.left
        return res

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
