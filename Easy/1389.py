class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        assert len(nums) == len(index)
        results = []
        for i in range(len(nums)):
            results.insert(index[i], nums[i])
        return results