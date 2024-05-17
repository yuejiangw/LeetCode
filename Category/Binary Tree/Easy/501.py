# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res = []
        self.pre = None
        self.count = 0
        self.max_count = 0

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # 不需要除了递归栈之外的额外空间
        def traversal(root):
            # 中序遍历 BST 可以得到一个非降序数组
            if not root:
                return
            traversal(root.left)

            if not self.pre:
                # 第一个节点
                self.count = 1
            elif self.pre.val == root.val:
                # 值相同的节点
                self.count += 1
            else:
                # 值不同的节点
                self.count = 1
            self.pre = root
            
            if self.count == self.max_count:
                self.res.append(root.val)
            if self.count > self.max_count:
                # 找到了更合适的候选人需要先清空 res
                self.max_count = self.count
                self.res.clear()
                self.res.append(root.val)

            traversal(root.right)
        
        traversal(root)
        return self.res
    

from collections import Counter
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        nums = []
        def traversal(root):
            if not root:
                return
            traversal(root.left)
            nums.append(root.val)
            traversal(root.right)
        traversal(root)
        counts = Counter(nums)
        mode_num = max(counts.values())
        res = []
        for k in counts.keys():
            if counts[k] == mode_num:
                res.append(k)
        return res