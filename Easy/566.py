from typing import List
    

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if r * c != row * col:
            return mat
        nums = [m[j] for m in mat for j in range(len(m))]
        res = [[0 for _ in range(c)] for _ in range(r)]
        k = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = nums[k]
                k += 1
        return res
