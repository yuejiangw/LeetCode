from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        位运算, 已知 int 型在计算机中占 32 位, 我们可以用一个长度为 32 位的数组来表示各个数字
        的加和. 这里用长度为 33 位的数组, 多出来的一位表示符号位. nums 中所有的数字按位加和,
        之后遍历 count 数组判断哪些位 mod 3 之后为 1, 如果为 1 则将其对应的位右移 i 位后加入
        到最终的结果中. 最后根据符号位调整结果的正负即可.
        """
        count = [0] * 33
        for num in nums:
            if num < 0:
                count[32] += 1
                num = -num
            for i in range(32):
                if (num >> i) & 1 == 1:
                    count[i] += 1
        res = 0
        for i in range(32):
            if count[i] % 3 == 1:
                res += (1 << i)
        return res if count[32] % 3 == 0 else -res
