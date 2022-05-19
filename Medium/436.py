from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = []  # 存储每个区间的开始坐标和在数组中的下标
        for i, interval in enumerate(intervals):
            start.append([interval[0], i])
        start = sorted(start, key=lambda x: x[0])

        def binary_search(start, target):
            left, right = 0, len(start) - 1
            while left <= right:
                mid = (right + left) // 2
                if (start[mid][0] == target):
                    return start[mid][1]
                elif start[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1 if left == len(start) else start[left][1]
        
        res = [-1] * len(intervals)
        for i, interval in enumerate(intervals):
            res[i] = binary_search(start, interval[1])
        return res

