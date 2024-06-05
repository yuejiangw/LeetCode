from typing import List
from heapq import *


class Solution:
    def convertArray(self, nums: List[int]) -> int:
        # Greedy，T: O(nlogn) S: O(n)
        def helper(nums):
            # helper function 用来求解把 nums 变成非递减数组需要多少步
            # 需要借助大顶堆
            res = 0
            heap = []
            for num in nums:
                if not heap:
                    heappush(heap, -num)
                else:
                    pre_max = -heap[0]
                    if pre_max > num:
                        # 如果前一个元素大于当前元素，则需要把前一个元素减小到当前元素
                        res += pre_max - num
                        # heappop + heapush，代表把堆顶元素（前一个元素）弹出，压入当前元素（类似于替换值）
                        heappushpop(heap, -num)
                    heappush(heap, -num)
            return res
        
        # 正向遍历一次 + 反向遍历一次，相当于覆盖非递减和非递增两种情况
        return min(helper(nums), helper(nums[::-1]))