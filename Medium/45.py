from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy，假设当前数组下标为 i，则它可以 cover 的最大距离是 i + nums[i]
        # 我们遍历 nums，每次跳跃要选 cover 最大的那个下标
        if len(nums) == 1:
            return 0
        i = 0
        cover = nums[0]
        res = 0
        while i < len(nums):
            # 当前元素的 cover 可以覆盖数组末尾
            if cover >= len(nums) - 1:
                return res + 1
            # 在 [i + 1, nums[i] + i] 中选 cover 最大的下标
            next = i + 1
            for j in range(i + 1, i + nums[i] + 1):
                if j + nums[j] >= cover:
                    next = j
                    cover = j + nums[j]
            i = next 
            res += 1
        return res


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        i = 0
        curr_cover = 0  # 当前覆盖的最远距离下标
        next_cover = 0  # 下一步覆盖的最远距离下标
        while i < len(nums):
            next_cover = max(next_cover, i + nums[i])
            # 已经走到了当前覆盖的最远处
            if i == curr_cover:
                if curr_cover != len(nums) - 1:
                    res += 1
                    curr_cover = next_cover
                    if next_cover >= len(nums) - 1:
                        break
                else:
                    break
            i += 1
        return res
