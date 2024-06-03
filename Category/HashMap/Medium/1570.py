from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        # 稀疏矩阵，我们只存储非零位置即可
        self.matrix = {}
        for idx, n in enumerate(nums):
            if n != 0:
                self.matrix[idx] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for k, v in self.matrix.items():
            if k in vec.matrix:
                res += v * vec.matrix[k]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
