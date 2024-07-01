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

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Rainbow Sort
        三个挡板
        [0, i) 包含所有 0
        [i, j) 包含所有 1
        [j, k] 是探索区域
        (k, len(nums) - 1] 包含所有 2
        
        三种情况：
        1. nums[j] == 0: 和 i 换位置，i += 1, j += 1
        2. nums[j] == 1, j += 1
        3. nums[j] == 2: 和 k 换位置，k -= 1

        example:
               k
        [0,0,1,1,2,2]
             i     
                 j
        """

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        i = 0
        j = 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                swap(i, j)
                i += 1
                j += 1
            elif nums[j] == 1:
                j += 1
            elif nums[j] == 2:
                swap(j, k)
                k -= 1
            
