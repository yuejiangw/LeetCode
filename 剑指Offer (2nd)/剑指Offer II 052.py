# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # T: O(N)
        # S: O(N)
        self.head = None
        self.pre = None

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if not self.head:
                self.head = root
            if self.pre:
                self.pre.right = root
                root.left = None
            self.pre = root
            inorder(root.right)
        
        inorder(root)
        return self.head
            