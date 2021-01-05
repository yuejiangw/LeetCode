class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        results = len(nums) * [0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[j] < nums[i]:
                        results[i] += 1
        return results
