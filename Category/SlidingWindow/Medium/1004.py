from typing import List


# 2023-07-10
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        题目翻译：求包含不超过 k 个 0 的最长子串的长度
        T: O(n)
        S: O(1)
        """
        l, r = 0, 0
        zero_num = 0
        res = 0
        while r < len(nums):
            # 窗口扩张
            c = nums[r]
            r += 1
            if c == 0:
                zero_num += 1
            # 窗口收缩
            while zero_num > k:
                d = nums[l]
                l += 1
                if d == 0:
                    zero_num -= 1
            # 收集结果
            if zero_num <= k:
                res = max(res, r - l)
        return res


# 2022-03-01
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Sliding Window, 找出一个最长的子数组, 该子数组内最多允许有 k 个0
        # T: O(N)
        # S: O(1)
        res = 0
        window = 0
        i, j = 0, 0
        while j < len(nums):
            c = nums[j]
            j += 1
            if c == 0:
                window += 1
            if window <= k:
                res = max(res, j - i)
            while i < j and window > k:
                d = nums[i]
                i += 1
                if d == 0:
                    window -= 1
        return res
