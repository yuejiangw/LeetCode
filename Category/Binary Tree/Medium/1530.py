# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # 遍历所有非叶节点 P，找到以 P 为最近公共祖先的所有叶子节点对并计算每一对之间的距离，统计距离不超过 distance 的数目
        # T: O(N * distance^2)
        # S: O(H * distance)
        self.ans = 0

        def dfs(root: TreeNode, distance: int) -> List[int]:
            # 此函数返回以 root 为根的所有叶子节点到 root 的距离的集合
            res = []
            if not root:
                return res
            
            # 叶子节点
            if not root.left and not root.right:
                res.append(1)
                return res
            
            l = dfs(root.left, distance)
            r = dfs(root.right, distance)
            
            # 对于左右子树中的距离，分别相加即为两个叶子节点之间的距离
            if l and r:
                for x in l:
                    for y in r:
                        # 叶节点之间的距离小于等于 distance 则收集结果
                        if x + y <= distance:
                            self.ans += 1
            
            # 此处的递归逻辑：一个叶子节点到 root 的距离 = 该叶子节点到 root.left / root.right  的距离 + 1
            # 多出来的这个 1 代表从 root.left / root.right 到 root 需要走一步
            for i in l:
                if i + 1 <= distance:
                    res.append(i + 1)
            for i in r:
                if i + 1 <= distance:
                    res.append(i + 1)
            return res    
            
        dfs(root, distance)
        return self.ans