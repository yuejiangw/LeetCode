from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(i):
            """ 判断每个小孩 i 个糖果时候是否满足需求 """
            if i == 0:
                return True
            count = 0   # count 代表最多可以满足的小孩的数量
            for c in candies:
                count += c // i
            return count >= k
        
        l, r = 0, max(candies) + 1
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1
