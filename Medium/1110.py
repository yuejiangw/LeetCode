# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.del_set = set(to_delete)
        self.res = []

        # 输入一颗二叉树, 删除 del_set 中的节点, 返回删除完成后的根节点
        def do_del(root, has_parent):
            if not root:
                return None
            # 判断是否需要被删除
            need_delete = root.val in self.del_set
            # 不需要删除而且没有父节点, 就是一个新的根节点
            if not need_delete and not has_parent:
                self.res.append(root)
            # 左右子树进行删除, 如果当前节点被删除了, 则其子节点就应该没有父节点
            # 所以 has_parent = not need_delete
            root.left = do_del(root.left, not need_delete)
            root.right = do_del(root.right, not need_delete)

            return None if need_delete else root

        do_del(root, False)
        return self.res            
