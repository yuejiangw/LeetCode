class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0 
        j = len(nums) - 1
        while i <= j:
            middle = (i + j) // 2
            if nums[middle] < target:
                i = middle + 1
            elif nums[middle] > target:
                j = middle - 1
            else:
                return middle
        return -1 