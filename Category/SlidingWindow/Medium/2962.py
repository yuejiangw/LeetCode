from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # sliding window
        target = max(nums)
        count = 0
        res = 0
        l, r = 0, 0
        while r < len(nums):
            c = nums[r]
            r += 1
            if c == target:
                count += 1
            while count == k:
                if nums[l] == target:
                    count -= 1
                l += 1
            # 每次加 l 是因为当前窗口内满足条件的子数组都可以和之前满足条件的子数组连起来凑成新的满足条件的子数组
            res += l
        return res
