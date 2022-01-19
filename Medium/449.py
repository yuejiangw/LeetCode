# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    直接将其用先序遍历序列化，因为是二叉搜索树，所以排序后就是中序遍历，
    因此反序列化就转换成了105题的从先序与中序构造二叉树的问题
    """

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        def preorder(root):
            if not root:
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        preorder = list(map(int, data.split(',')))
        inorder = sorted(preorder)

        def build_tree(preorder, inorder):
            if not preorder:
                return None
            root_val = preorder[0]
            root_idx = inorder.index(root_val)
            root = TreeNode(root_val)
            root.left = build_tree(
                preorder[1: root_idx + 1], inorder[:root_idx])
            root.right = build_tree(
                preorder[root_idx + 1:], inorder[root_idx + 1:])
            return root
        return build_tree(preorder, inorder)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
