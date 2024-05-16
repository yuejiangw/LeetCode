# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 借助全局最大值来进行比较
    max_val = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST 性质: 中序遍历会得到一个从小到大的有序数组
        # 我们用 max_val 代表遍历过的节点中的最大值
        def traversal(root):
            if not root:
                return True
            # 中序遍历
            left = traversal(root.left)
            # 如果当前节点的值小于等于 max_val 则说明不是 BST
            if root.val <= self.max_val:
                return False
            else:
                self.max_val = root.val
            right = traversal(root.right)
            return left and right
        
        return traversal(root)
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        path = []
        def inorder_traverse(root):
            if not root:
                return
            inorder_traverse(root.left)
            path.append(root.val)
            inorder_traverse(root.right)
        if not root:
            return True
        inorder_traverse(root)
        for i in range(1, len(path)):
            # 要用 <=，因为不能有重复元素
            if path[i] <= path[i - 1]:
                return False
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid(root, min_node, max_node):
            if not root:
                return True
            if min_node and root.val <= min_node.val:
                return False
            if max_node and root.val >= max_node.val:
                return False
            return is_valid(root.left, min_node, root) \
                    and is_valid(root.right, root, max_node) 
        
        return is_valid(root, None, None)