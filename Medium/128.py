from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # T: O(N), S: O(N)
        nums = set(nums)
        res = 0
        for num in nums:
            # 从序列起点开始找
            if num - 1 not in nums:
                curr = num
                curr_len = 1
                # 持续查找 num + 1, num + 2, ... 是否在 set 里
                while curr + 1 in nums:
                    curr += 1
                    curr_len += 1
                res = max(res, curr_len)
        return res