from typing import List


class Solution:
    """
    窗口扩张：更新窗口内元素数量和元素总和
    窗口收缩：窗口内的元素数量大于 k 时，窗口收缩并更新窗口内元素数量和元素总和
    更新结果：窗口内的元素数量等于 k 时，取已有 res 值和现有窗口 avg 值的较大者
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")
        window_sum, count = 0, 0
        i, j = 0, 0
        while j < len(nums):
            # 窗口扩张
            c = nums[j]
            j += 1
            window_sum += c
            count += 1
            # 窗口收缩
            if count > k:
                d = nums[i]
                i += 1
                window_sum -= d
                count -= 1
            # 更新结果
            if count == k:
                res = max(res, window_sum / count)
        return res
