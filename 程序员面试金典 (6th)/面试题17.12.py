# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
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


