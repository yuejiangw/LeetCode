from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # 差分数组, 每个元素存储的是与数组前一个元素的差值
        # 假如原始数组为arr, 差分数组为diff_arr, 则
        # diff_arr[i] = arr[i] - arr[i-1]
        diff_array = [0 for _ in range(length)]

        # 更新差分数组
        # 由update的定义可知, start下标的元素比start-1下标的元素大inc
        # end+1下标的元素比end下标的元素小inc
        for start, end, inc in updates:
            diff_array[start] += inc
            if end + 1 < length:
                diff_array[end+1] -= inc

        # 根据差分数组还原数组
        for i in range(1, length):
            diff_array[i] += diff_array[i-1]
        return diff_array
