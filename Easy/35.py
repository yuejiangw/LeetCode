class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not target in nums:
            for i, v in enumerate(nums):
                if v < target:
                    if i == len(nums) - 1:
                        nums.append(target)
                        break
                    else:
                        continue
                else:
                    nums.insert(i, target)
                    break
        return nums.index(target)
