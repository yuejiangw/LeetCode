from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        target = max(nums)
        l = r = 0
        cnt = res = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            if c == target:
                cnt += 1
            while cnt >= k:
                d = nums[l]
                l += 1
                if d == target:
                    cnt -= 1
            res += l
        return res