# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 未找到删除节点直接返回空
        if not root:
            return root
        if root.val == key:
            # 左右都为空则返回空
            if not root.left and not root.right:
                return None
            # 左子树为空则返回右子树
            elif not root.left:
                return root.right
            # 右子树为空则返回左子树
            elif not root.right:
                return root.left
            # 左右子树都不为空则把左子树挂在右子树中最小节点下左子树的位置
            # 右子树为新的根节点
            else:
                curr = root.right
                # 找最小
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                return root.right
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root

class Solution:
    def find_min(self, root) -> TreeNode:
        curr = root
        while curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None: return root.right
            if root.right is None: return root.left
            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, root.val)
        return root