class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 使用两个指针来分别交换 0 和 1，用 p0 和 p1 表示
        # 如果找到了 1 就与 nums[p1] 元素交换，同时 p1 右移一个位置
        # 如果找到了 0，要注意 p0 和 p1 的位置关系
        # 如果此时 p0 < p1，则 nums[p0] 与 nums[i] 交换后一定会把一个 1 交换出去，这时应该再次将 nums[i] 与 nums[p1] 交换
        # 并且找到了 0 之后我们要同时移动 p0 和 p1
        p0, p1 = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                nums[p1], nums[i] = nums[i], nums[p1]
                p1 += 1
            elif nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                if p0 < p1:
                    nums[p1], nums[i] = nums[i], nums[p1]
                p0 += 1
                p1 += 1

