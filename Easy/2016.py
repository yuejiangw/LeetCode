from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        """
        股票问题的翻版, 在遍历的过程中取当前下标左部分的最小值和右部分的最大值进行计算
        时间复杂度: O(N)
        空间复杂度: O(1)
        """
        res = -1
        min_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > min_num:
                res = max(res, nums[i] - min_num)
            else:
                min_num = nums[i]
        return res