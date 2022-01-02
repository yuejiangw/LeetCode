from typing import List


class Solution:
    """ O(nlogn), sort """
    def minArray(self, numbers: List[int]) -> int:
        return sorted(numbers)[0]


class Solution:
    """ O(n), iterate """
    def minArray(self, numbers: List[int]) -> int:
        res = numbers[0]
        for i in range(len(numbers)-1):
            if numbers[i+1] < numbers[i]:
                res = numbers[i+1]
                break
        return res


class Solution:
    """ O(logn), binary search """
    def minArray(self, numbers: List[int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            mid = i + (j - i) // 2
            if numbers[mid] > numbers[j]:
                i = mid + 1
            elif numbers[mid] < numbers[j]:
                j = mid
            else:
                j -= 1
        return numbers[i]
