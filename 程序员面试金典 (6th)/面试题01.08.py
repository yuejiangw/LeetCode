class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return None
        # 找出所有为0的元素，记录其下标
        zero_index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_index.append((i, j))

        # 对zero_index进行筛选，找出所有不同的行和列
        row = set([zero[0] for zero in zero_index])
        col = set([zero[1] for zero in zero_index])

        # 对行和列置0
        for i in row:
            matrix[i] = [0] * len(matrix[0])
        for j in col:
            for i in range(len(matrix)):
                matrix[i][j] = 0