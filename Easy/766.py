class Solution:
    '''
    只需判断前行中除最后一个元素外剩余的元素是否完全等于后行中除第一个元素外剩余的元素。
    '''
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        if col == 1 or row == 1:
            return True
        for i in range(row - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True