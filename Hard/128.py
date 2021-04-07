class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        # 先去掉重复的数据
        nums = sorted(list(set(nums)))
        length = 1
        result = []
        pre_offset = nums[0]
        for i in range(1, len(nums)):
            cur_offset = nums[i] - i
            if cur_offset == pre_offset:
                length += 1
            else:
                result.append(length)
                pre_offset = cur_offset
                length = 1
        result.append(length)
        return max(result)