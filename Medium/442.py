from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """思路
        nums 数组中的每一个元素的值的范围都在[1, n]，所以可以把元素值 - 1映射到数组下标
        利用数组中元素的正负判断当前元素是否已经被访问过
        """
        # T: O(N)
        # S: O(1)
        res = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                res.append(n)
            else:
                nums[n - 1] = -nums[n - 1]
        return res