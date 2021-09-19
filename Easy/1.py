class Solution:
    """暴力解，时间复杂度O(n^2)"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    """哈希表，时间复杂度O(nlogn)"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            hashmap[num] = idx
        for idx, num in enumerate(nums):
            remain = target - num
            if remain in hashmap.keys() and idx != hashmap[remain]:
                return [idx, hashmap[remain]]