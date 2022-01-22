# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        # base case: 如果树里只有一个根节点，则直接返回 root.val
        if not root.left and not root.right:
            return root.val

        parent = {}
        target_node = None

        def traverse(root, parent_node):
            """ 记录树中各节点与其父节点的对应关系，同时找到 k 对应的节点 """
            nonlocal target_node
            if not root:
                return
            if root.val == k:
                target_node = root
            # node 的 val 唯一，因此可以用来做哈希表中的 key
            parent[root.val] = parent_node
            traverse(root.left, root)
            traverse(root.right, root)

        # 执行辅助函数
        traverse(root, None)

        # 从 target_node 开始进行 bfs
        queue = deque()
        visited = set()
        queue.append(target_node)
        visited.add(k)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                # 找到叶子节点，则直接返回
                if not node.left and not node.right:
                    return node.val
                # bfs，向该节点的父节点，左右子树扩散
                parent_node = parent[node.val]
                if parent_node and parent_node.val not in visited:
                    queue.append(parent_node)
                    visited.add(parent_node.val)
                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                    visited.add(node.left.val)
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                    visited.add(node.right.val)
        return -1
