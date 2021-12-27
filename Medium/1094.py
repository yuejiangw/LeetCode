from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        差分数组，需要注意的一点是在 end 时刻，乘客已经下车了，所以数组中是
        diff_arr[end] -= num 而不是 diff_arr[end+1] -= num
        """
        length = max(trips, key=lambda x: x[2])[2] + 1
        diff_arr = [0 for _ in range(length)]

        for num, start, end in trips:
            diff_arr[start] += num
            diff_arr[end] -= num
        for i in range(1, length):
            diff_arr[i] += diff_arr[i - 1]

        return max(diff_arr) <= capacity
