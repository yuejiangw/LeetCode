from typing import List


class Solution:
    def count_sort(self, nums: List[int]) -> List[int]:
        """计数排序
        T: O(n)
        S: O(n)
        """
        # 取 nums 中的最大值和最小值, 以此来确定 count 数组的长度
        min_num, max_num = min(nums), max(nums)
        n = max_num - min_num + 1
        count = [0] * n
        # 对于 nums 中的每个元素, 计算其与 min_num 的偏移量作为 count 数组中的下标进行计数
        for num in nums:
            count[num - min_num] += 1
        # 从头开始遍历 count 数组, 根据当前下标与 min_num 来还原原始的数组值, 修改 nums 数组
        index = 0
        for idx, cnt in enumerate(count):
            while cnt:
                nums[index] = idx + min_num
                cnt -= 1
                index += 1
        return nums

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.count_sort(nums)