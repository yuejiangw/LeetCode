class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        for i in range(1, rowIndex + 1):
            path = [1] * (i + 1)
            for j in range(1, i):
                path[j] = res[i - 1][j] + res[i - 1][j - 1]
            res.append(path)
        return res[-1]