# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 前缀和, T: O(N), S: O(N)
        def dfs(node, curr_sum):
            # 在遍历路径时记录前缀和，如果某个路径的前缀和与目标和的差值等于某个之前的前缀和，
            # 则说明从从那个前缀和开始到当前节点的路径和等于 targetSum
            if not node:
                return 0
            # 当前前缀和
            curr_sum += node.val
            # 从当前节点出发的有效路径数量
            count = prefix_sum.get(curr_sum - targetSum, 0)
            # 更新当前路径和的次数
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
            # 继续向左右子树递归
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # 回溯时移除当前节点的前缀和次数
            prefix_sum[curr_sum] -= 1

            return count

        # 存储前缀和出现的次数
        prefix_sum = {0: 1}
        return dfs(root, 0)



class Solution:
    """ 双重递归，首先先序遍历每个节点，再以每个节点作为起始点递归寻找满足条件的路径 """
    res = 0

    def dfs(self, root, targetSum):
        if not root:
            return
        if root.val == targetSum:
            self.res += 1
        self.dfs(root.left, targetSum - root.val)
        self.dfs(root.right, targetSum - root.val)

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        # T: O(N^2), S: O(N)
        if not root:
            return 0
        self.dfs(root, targetSum)
        # 由于路径不需要从 root 开始，因此第二个参数为 targetSum，不是 targetSum - root.val
        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)
        return self.res
