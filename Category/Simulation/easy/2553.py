from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        nums_list = [list(str(x)) for x in nums]
        res = nums_list[0]
        for i in range(1, len(nums_list)):
            res += nums_list[i]
        return list(map(int, res))
