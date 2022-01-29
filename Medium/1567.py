from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # 正数个数，负数个数，第一次出现负数的下标
        pos, neg, first_neg_idx = 0, 0, -1
        res = 0
        # 贪心策略：如果负数个数为偶数个，则子数组长度=正数个数+负数个数；
        # 如果负数个数为奇数个，则应删除第一个负数，子数组长度=当前下标-第一次出现负数的下标
        # 如果遇到0，则重新开始计数，因为0乘任何数都是0，不是正数
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
            elif nums[i] < 0:
                if first_neg_idx == -1:
                    first_neg_idx = i
                neg += 1
            else:
                pos, neg, first_neg_idx = 0, 0, -1

            if neg % 2 == 0:
                res = max(res, pos + neg)
            else:
                res = max(res, i - first_neg_idx)
        return res
