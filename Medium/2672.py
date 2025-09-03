from collections import deque
from typing import List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # 滑动窗口 + 两个单调队列
        l = r = 0
        # 存下标，保持队首最大/小
        maxdq = deque()
        mindq = deque()
        res = 0
        while r < len(nums):
            c = nums[r]
            
            # 更新单调队列确认当前窗口内的最大/小值
            while maxdq and nums[maxdq[-1]] < c:
                maxdq.pop()
            maxdq.append(r)
            
            while mindq and nums[mindq[-1]] > c:
                mindq.pop()
            mindq.append(r)

            r += 1

            # 收缩窗口
            while maxdq and mindq and nums[maxdq[0]] - nums[mindq[0]] > 2:
                if maxdq[0] == l:
                    maxdq.popleft()
                if mindq[0] == l:
                    mindq.popleft()
                l += 1

            res += r - l
        return res