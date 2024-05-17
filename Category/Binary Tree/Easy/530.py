# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        path = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            path.append(root.val)
            traversal(root.right)
        traversal(root)
        res = float('inf')
        for i in range(1, len(path)):
            res = min(res, path[i] - path[i - 1])
        return res

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 思路：中序遍历可以得到一个有序数组，在有序数组中找最小差值一定是两个相邻的元素之间的差值
        stack = deque()
        pre = None
        curr = root
        res = float('inf')
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if pre:
                    res = min(res, curr.val - pre.val)
                pre = curr
                curr = curr.right
        return res