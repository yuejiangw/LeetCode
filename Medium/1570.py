from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.index = set()
        self.vector = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.index.add(i)
                self.vector[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        valid_idx = self.index & vec.index
        res = 0
        for i in valid_idx:
            res += self.vector[i] * vec.vector[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
