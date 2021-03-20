class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        nums = []
        for i in range(row):
            for j in range(col):
                nums.append(matrix[i][j])
        return sorted(nums)[k-1]