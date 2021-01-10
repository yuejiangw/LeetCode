class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        
        candidates = []
        for i in set(nums):
            if nums.count(i) >= 2:
                candidates.append(i)

        for c in candidates:
            i = 0
            while i < nums.count(c):
                index1 = nums.index(c)
                nums.pop(index1)
                index2 = nums.index(c)
                if (index2 - index1 + 1) <= k:
                    return True
                i += 1
            return False