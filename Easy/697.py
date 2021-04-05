class Solution:
    def getMode(self, nums):
        # 获取数组nums的度
        candidates = [nums.count(n) for n in set(nums)]
        degree = max(candidates)
        # 返回该数组的众数
        mode = []
        for i in range(len(candidates)):
            if candidates[i] == degree:
                mode.append(list(set(nums))[i])
        return mode

    def findShortestSubArray(self, nums: List[int]) -> int:
        mode = self.getMode(nums)
        candidates = []
        # 本质上就是求该数组中众数第一次出现的位置和最后一次出现的位置
        for n in mode:
            pos1 = nums.index(n)
            pos2 = len(nums) - nums[::-1].index(n) - 1
            candidates.append(pos2 - pos1 + 1)
        return min(candidates)