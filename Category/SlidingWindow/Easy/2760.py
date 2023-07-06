from typing import List


class Solution:
    """
    由于此题要求 nums[l] 必须为偶数，因此这道题应该以左边界指针 l 作为退出循环的条件。
    首先 l 不断左移直到找到一个满足条件的起始位置，之后右边界指针 r 从这个位置开始扫描，
    直到遇到不满足条件的值，此时退出循环并更新 res。

    由于 r 退出循环代表遇到了不符合条件的值，因此从 l 到 r 的这个区间可以直接跳过扫描，
    l 的值可以直接设置成 r。

    T: O(N)
    S: O(1)
    """

    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = 0
        l, r = 0, 0
        while l < len(nums):
            while l < len(nums) and (nums[l] % 2 == 1 or nums[l] > threshold):
                l += 1
            if l < len(nums):
                r = l + 1
                while (
                    r < len(nums)
                    and nums[r] % 2 != nums[r - 1] % 2
                    and nums[r] <= threshold
                ):
                    r += 1
                res = max(res, r - l)
                l = r
        return res
