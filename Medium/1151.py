from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # 维护一个固定长度的 sliding window，找到包含 1 最多的 window
        # T: O(n)
        # S: O(1)
        ones = sum(data)
        cnt_one = max_one = 0
        left = right = 0
        while right < len(data):
            cnt_one += data[right]
            right += 1
            if right - left > ones:
                cnt_one -= data[left]
                left += 1
            max_one = max(max_one, cnt_one)
        return ones - max_one