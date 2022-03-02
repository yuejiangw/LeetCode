# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # 层序遍历，设置一个停止标志，遇到空节点，停止标志为真，
        # 如果停止标志为真，再遍历遇到非空节点，则非完全二叉树
        # T: O(N)
        # S: O(N)
        if not root:
            return True
        queue = deque()
        queue.append(root)
        is_stop = False
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                
                if node.left:
                    if is_stop:
                        return False
                    queue.append(node.left)
                else:
                    is_stop = True

                if node.right:
                    if is_stop:
                        return False
                    queue.append(node.right)
                else:
                    is_stop = True

        return True
