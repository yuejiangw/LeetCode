from typing import List

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
