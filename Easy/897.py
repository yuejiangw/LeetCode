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
        nodes = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nodes.append(TreeNode(root.val))
            inorder(root.right)
        
        inorder(root)

        if not nodes:
            return None
        head = nodes[0]
        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i + 1]
        return head
