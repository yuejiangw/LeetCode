# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """ 思路: 将树转换为一个图，进行 BFS 搜索 """
        parent = {}

        def traverse(root: TreeNode, parent_node: TreeNode):
            """ 递归记录每个节点的父节点 """
            if not root:
                return
            parent[root.val] = parent_node
            traverse(root.left, root)
            traverse(root.right, root)

        traverse(root, None)
        # 开始从 target 节点施放 BFS 算法
        res = []
        queue = deque()
        visited = set()
        queue.append(target)
        visited.add(target.val)
        step = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                # 当 step == k 的时候收集结果
                if step == k:
                    res.append(node.val)
                # bfs, 向父节点和左右子树扩散
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
            step += 1
        return res
