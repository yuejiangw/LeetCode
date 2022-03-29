# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                curr.left = root.left
                root = root.right
                return root
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