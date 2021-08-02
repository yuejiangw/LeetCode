from typing import List
from functools import cmp_to_key

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        nums = [str(x) for x in nums]
        sorted_nums = sorted(nums, key=cmp_to_key(sort_rule))
        return ''.join(sorted_nums)
        

if __name__ == '__main__':
    sol = Solution()
    test = [3, 31, 34, 30, 5, 9]
    sol.minNumber(test)