from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        res = 0

        def traverse(code, path):
            """ 遍历二叉树，顺便记录遍历过的路径之和 """
            nonlocal res
            if code not in tree:
                return
            # 当前遍历到的节点值
            value = tree[code]
            # 当前节点的深度和 id
            depth, id = code // 10, code % 10
            # 左右子树的编码
            left = 10 * (depth + 1) + (id * 2 - 1)
            right = 10 * (depth + 1) + (id * 2)
            # 到达叶子节点，收集结果，返回
            if left not in tree and right not in tree:
                res += path + value
                return
            # 二叉树递归遍历
            traverse(left, path + value)
            traverse(right, path + value)

        for code in nums:
            value = code % 10
            code = code // 10
            tree[code] = value
        root_code = nums[0] // 10
        traverse(root_code, 0)
        return res
