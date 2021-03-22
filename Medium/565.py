class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        flags = [False] * len(nums)
        links = []
        while flags.count(True) < len(nums):
            i = flags.index(False)
            tmp = []
            while nums[i] not in tmp:
                tmp.append(nums[i])
                flags[i] = True
                i = nums[i]

            links.append(tmp)
        return max([len(l) for l in links])