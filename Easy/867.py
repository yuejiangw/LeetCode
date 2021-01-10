class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        row = len(A)
        col = len(A[0])
        for i in range(col):
            result.append([])
        for i in range(row):
            for j in range(col):
                result[j].append(A[i][j])
        return result