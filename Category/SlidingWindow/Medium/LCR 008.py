class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        window = 0
        res = float('inf')
        while r < len(nums):
            c = nums[r]
            r += 1
            window += c
            while window >= target:
                res = min(res, r - l)
                d = nums[l]
                l += 1
                window -= d
        return res if res != float('inf') else 0