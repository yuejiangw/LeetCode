from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # T: O(n), S: O(1)
        # 思路：众数出现的次数最多，遇到众数则计数器 + 1，否则 - 1，如果最后计数器为正，则说明选择的 target 就是众数
        target = 0
        count = 0
        for n in nums:
            if count == 0:
                target = n
                count = 1
            elif n == target:
                count += 1
            else:
                count -= 1
        return target