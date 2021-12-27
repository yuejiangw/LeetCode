from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        sum = 0
        res = 0
        for num in nums:
            sum += num
            if (sum - k) in count:
                res += count[sum-k]
            if sum in count:
                count[sum] += 1
            else:
                count[sum] = 1
        return res
