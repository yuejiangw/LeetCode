from typing import List


class Solution:
    """
    ^: xor
    0 ^ x = x
    a ^ (a ^ c) = (a ^ a) ^ c
    a ^ a = 0
    最后剩下的一个数就是落单的数字
    """
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res