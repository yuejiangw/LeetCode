class Solution:
    def getMode(self, nums):
        candidates = [nums.count(n) for n in set(nums)]
        degree = max(candidates)
        mode = []
        for i in range(len(candidates)):
            if candidates[i] == degree:
                mode.append(list(set(nums))[i])
        return mode

    def findShortestSubArray(self, nums: List[int]) -> int:
        mode = self.getMode(nums)
        candidates = []
        for n in mode:
            pos1 = nums.index(n)
            pos2 = len(nums) - nums[::-1].index(n) - 1
            candidates.append(pos2 - pos1 + 1)
        return min(candidates)