from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            # 最小的数都比0大，直接退出
            if nums[i] > 0:
                return res
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            # 双指针
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # 左右指针去重
                    while left != right and nums[left] == nums[left + 1]:
                        left += 1
                    while left != right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        固定住第一个元素，然后对后续元素进行twoSum，注意去重 
        """
        def two_sum(nums, start, target):
            res = []
            i, j = start, len(nums) - 1
            while i < j:
                tmp = nums[i] + nums[j]
                left, right = nums[i], nums[j]
                if tmp < target:
                    # 去重
                    while i < j and nums[i] == left:
                        i += 1
                elif tmp > target:
                    # 去重
                    while i < j and nums[j] == right:
                        j -= 1
                else:
                    res.append([i, j])
                    # 去重
                    while i < j and nums[i] == left:
                        i += 1
                    while i < j and nums[j] == right:
                        j -= 1
            return res

        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            # 最小的数都比0大，直接退出
            if nums[i] > 0:
                break
            tuples = two_sum(nums, i + 1, -nums[i])
            for j, k in tuples:
                res.append([nums[i], nums[j], nums[k]])
            # 去重
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return res

# 2024.04.24
class Solution:
    """通用解法，nSum"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 数组要先排序，之后用双指针
        def nSum(n: int, nums: List[int], start: int, target: int):
            if n == 2:
                i, j = start, len(nums) - 1
                res = []
                while i < j:
                    m, n = nums[i], nums[j]
                    if m + n < target:
                        i += 1
                    elif m + n > target:
                        j -= 1
                    else:
                        res.append([m, n])
                        # 去重
                        while i < j and nums[i] == m: i += 1
                        while i < j and nums[j] == n: j -= 1
                return res
            else:
                res = []
                i = start
                while i < len(nums):
                    tmp_result = nSum(n - 1, nums, i + 1, target - nums[i])
                    for tmp in tmp_result:
                        tmp.append(nums[i])
                        res.append(tmp)
                    # 去重
                    while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                        i += 1
                    i += 1
                return res
        
        nums.sort()
        return nSum(3, nums, 0, 0)