import imp
from multiprocessing.spawn import import_main_path
from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # Time complexity: O(NlogN)
        # Space complexity: O(1)

        def check(length):
            cnt = 0
            for ribbon in ribbons:
                cnt += ribbon // length
            if cnt >= k:
                return True
            return False
        
        # 二分查找
        # 思路: 本质上是从1开始枚举所有切割后的长度可能, 那么最大的可能长度就是所有绳长中的最大值
        # 可以利用二分搜索的思路优化算法, 在取中点值后判断以该值作为切割长度能否使切割过后的总数量
        # 达到k; 如果可以则说明mid是一个潜在的结果,我们要继续向其右侧寻找,否则说明mid的值过大,应该
        # 向其左侧寻找
        l, r = 1, max(ribbons)
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res
