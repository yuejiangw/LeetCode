from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        1. a represents for the min element, b is the second largest number
        2. keep updating a, and make b as small as possible
        3. If the next element is larger than b, then return True
        """
        a = float('inf')
        b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False
