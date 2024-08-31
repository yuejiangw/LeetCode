from typing import List

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        '''
        nums = [113, 215, 221]
             11
            /   \
           21    22
           / \   / \
          31 32 33  34

        dfs -> 
        {
            11: 1
            21: 1
            22: 2
        }

        13 -> 2(2*1-1, 2*1)
        '''
        tree = {}
        for num in nums:
            value = num % 10
            code = num // 10
            # {key: level + idx, val: value}
            tree[code] = value
        
        self.res = 0
        def traversal(code, path):
            if code not in tree:
                return
            # 当前遍历到的节点的值
            value = tree[code]
            # 当前节点的深度和 idx
            depth, idx = code // 10, code % 10
            # 左右子树编码
            left = 10 * (depth + 1) + (2 * idx - 1)
            right = 10 * (depth + 1) + (2 * idx)
            # 到达叶子节点收集结果并返回
            if left not in tree and right not in tree:
                self.res += path + value
                return
            # 递归
            traversal(left, path + value)
            traversal(right, path + value)

        root_code = nums[0] // 10
        traversal(root_code, 0)
        return self.res