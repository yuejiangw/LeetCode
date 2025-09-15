# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        res = root
        curr_depth = 0
        queue = deque()
        if depth == 1:
            res = TreeNode(val, root, None)
            queue.append(res)
        else:
            queue.append(root)
        while queue:
            curr_depth += 1
            l = len(queue)
            for _ in range(l):
                curr = queue.popleft()
                if curr_depth == depth - 1:
                    left_ndoe = TreeNode(val, curr.left, None)
                    right_node = TreeNode(val, None, curr.right)
                    curr.left, curr.right = left_ndoe, right_node
                    queue.append(left_ndoe)
                    queue.append(right_node)
                else:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        return res