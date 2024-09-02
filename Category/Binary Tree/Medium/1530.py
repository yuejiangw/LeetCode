# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        '''
        举例说明为什么在 traversal 函数中，当 root 恰好为 leaf node 的时候返回 [1]

            1
           / \
           2  3
          [1] [1]
        
        如上所示的二叉树，在 traversal(2) 和 traversal(3) 的时候，都返回 [1]，则在 traversal(1) 的时候
        我们的 left 和 right 就分别是 [1] 和 [1]，直接代表了叶子节点到根节点之间的距离
        这样一来，我们在计算 path 的时候就可以直接用 left 和 right 中的 value 相加

        如果为了使 distance 的定义统一，在 root 即为 leaf 的时候返回 [0]，则最后在判断是否可以更新结果的时候，就要
        写成 if x + y + 2 <= distance
        '''
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