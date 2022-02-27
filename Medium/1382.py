# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 先中序遍历, 获取一个升序序列, 再基于这个升序序列构造平衡BST
        # 时间复杂度 O(N), 空间复杂度 O(N), 因为需要额外的数组存储节点值
        
        values = []
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            values.append(root.val)
            inorder(root.right)
        
        inorder(root)

        def build(values):
            if not values:
                return None
            mid = len(values) // 2
            root = TreeNode(values[mid])
            root.left = build(values[:mid])
            root.right = build(values[mid + 1:])
            return root
        
        return build(values)
