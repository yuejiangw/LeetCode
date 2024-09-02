from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_num = len(set(nums))
        i, j = 0, 0
        window = {}
        res = 0
        
        while j < len(nums):
            c = nums[j]
            j += 1
            if c not in window:
                window[c] = 0
            window[c] += 1
            
            while i < j and len(window) == distinct_num:
                d = nums[i]
                i += 1
                window[d] -= 1
                if window[d] == 0:
                    del window[d]
            res += i    # 子数组左端点 < i 的都是合法的

        return res