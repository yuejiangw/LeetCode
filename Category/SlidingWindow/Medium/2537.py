from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        '''
        如果窗口中有 c 个元素 x，再进来一个 x，会新增 c 个相等数对。
        如果窗口中有 c 个元素 x，再去掉一个 x，会减少 c−1 个相等数对。
        '''
        l = r = 0
        window = defaultdict(int)
        res = 0
        pair = 0
        while r < len(nums):
            c = nums[r]
            r += 1
            pair += window[c]
            window[c] += 1
            while pair >= k:
                d = nums[l]
                l += 1
                pair -= (window[d] - 1)
                window[d] -= 1
            res += l
        return res