# 排序之后最大乘积就两种情况：
# 1、如果全是正数就是最后三个数相乘 
# 2、如果有负数最大的乘机要么是最后三个数相乘，要么是两个最小的负数相乘再乘以最大的正数
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        p1 = nums[-1] * nums[-2] * nums[-3]
        p2 = nums[0] * nums[1] * nums[-1]
        return max(p1, p2)