# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """暴力层序遍历解"""
        if not root:
            return 0
        count = 0
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                count += 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return count

class Solution:
    """
    利用完全二叉树的性质求解
    完全二叉树要么是满二叉树，要么除了最后一层其它层合在一起是满二叉树
    还是按照层序遍历的思路遍历，同时记录满二叉树的层数
    遇到非满的结点时就停止遍历，最后总结点数量即为满二叉树结点数量加队列内剩余的节点数量
    """
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        level_num = 0
        flag = True
        while flag and queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left is not None and node.right is not None:
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.left is not None and node.right is None:
                    queue.append(node.left)
                    flag = False
                elif node.right is not None and node.left is None:
                    queue.append(node.right)
                    flag = False
                else:
                    flag = False
            level_num += 1
        return len(queue) + 2 ** level_num - 1