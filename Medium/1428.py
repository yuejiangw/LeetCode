# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # 从右下角开始，遇到1往左走，遇到0往上走，走到第一行
        # T: O(row + col)
        # S: O(1)
        row, col = binaryMatrix.dimensions()
        i, j = row - 1, col - 1
        res = -1
        while i >= 0 and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                res = j
                j -= 1
            else:
                i -= 1
        return res
