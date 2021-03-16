class Solution:
    def lowerBound(self, nums: List[int], target: int) -> int:
        low = 0
        up = len(nums)
        while low < up:
            mid = (low + up) // 2
            if nums[mid] >= target:
                up = mid
            else:
                low = mid + 1
        return low
    
    def upperBound(self, nums: List[int], target: int) -> int:
        low = 0
        up = len(nums)
        while low < up:
            mid = (low + up) // 2
            if nums[mid] > target:
                up = mid
            else:
                low = mid + 1
        return low

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        else:
            low = self.lowerBound(nums, target)
            up = self.upperBound(nums, target) - 1
            if low == len(nums) or nums[low] != target:
                return [-1, -1]
            return [low, up]        