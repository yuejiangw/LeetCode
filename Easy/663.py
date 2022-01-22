# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        """
        首先求出整棵树的所有节点值的和，之后检查每个节点，
        判断以该节点为根的子树的值的和是否等于整棵树所有节点值的和的一半
        """
        if not root:
            return False

        subtree_sum = set()

        def get_sum(root):
            if not root:
                return 0
            left, right = get_sum(root.left), get_sum(root.right)
            root_sum = left + right + root.val
            subtree_sum.add(root_sum)
            return root_sum
            
        # 这里不能直接用get_sum(root)，否则当节点值总和为0的时候会有错误
        tree_sum = root.val + get_sum(root.left) + get_sum(root.right)
        if tree_sum % 2 != 0:
            return False
        return (tree_sum // 2) in subtree_sum
