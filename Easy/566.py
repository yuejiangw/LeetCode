class Solution:
    def getElements(self, nums):
        m = len(nums)
        n = len(nums[0])
        result = []
        for i in range(m):
            for j in range(n):
                result.append(nums[i][j])
        return result

    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(nums)
        n = len(nums[0])
        if m * n != r * c:
            return nums
        result = self.getElements(nums)
        new_matrix = [[0 for i in range(c)] for j in range(r)]
        counter = 0
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = result[counter]
                counter += 1
        return new_matrix