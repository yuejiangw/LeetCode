from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_2_num = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.idx_2_num[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k, v in self.idx_2_num.items():
            if k in vec.idx_2_num:
                res += v * vec.idx_2_num[k]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)