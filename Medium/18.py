from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """ 固定住第一个元素，对后续元素进行threeSum，注意去重 """
        def three_sum(nums, start, target):
            def two_sum(numbers, start_idx, target):
                res = []
                i, j = start_idx, len(numbers) - 1
                while i < j:
                    tmp = numbers[i] + numbers[j]
                    left, right = numbers[i], numbers[j]
                    if tmp < target:
                        while i < j and numbers[i] == left: i += 1
                    elif tmp > target:
                        while i < j and numbers[j] == right: j -= 1
                    else:
                        res.append([i, j])
                        while i < j and numbers[i] == left: i += 1
                        while i < j and numbers[j] == right: j -= 1
                return res
            res = [] 
            i = start
            while i < len(nums):
                tuples = two_sum(nums, i + 1, target - nums[i])
                for j, k in tuples:
                    res.append([i, j, k])
                while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                    i += 1
                i += 1
            return res


        nums.sort()
        res = []
        a = 0
        while a < len(nums):
            tuples = three_sum(nums, a + 1, target - nums[a])
            for b, c, d in tuples:
                res.append([nums[a], nums[b], nums[c], nums[d]])
            while a < len(nums) - 1 and nums[a + 1] == nums[a]:
                a += 1
            a += 1
        return res
    
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        通用解法
        T: O(N^3), S: O(N)
        """
        def nSum(nums, n, start, target):
            res = []
            if n < 2:
                return res
            if n == 2:
                i, j = start, len(nums) - 1
                while i < j:
                    curr = nums[i] + nums[j]
                    left, right = nums[i], nums[j]
                    if curr < target:
                        # 去重
                        while i < j and nums[i] == left:
                            i += 1
                    elif curr > target:
                        # 去重
                        while i < j and nums[j] == right:
                            j -= 1
                    else:
                        res.append([left, right])
                        # 去重
                        while i < j and nums[i] == left:
                            i += 1
                        while i < j and nums[j] == right:
                            j -= 1
                return res
            else:
                i = start
                while i < len(nums):
                    tmp = nSum(nums, n - 1, i + 1, target - nums[i])
                    for tmp_res in tmp:
                        tmp_res.append(nums[i])
                        res.append(tmp_res)
                    # 去重
                    while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                        i += 1
                    i += 1
            return res
        
        nums.sort()
        return nSum(nums, 4, 0, target)
