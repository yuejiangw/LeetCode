from typing import List
class Solution:
    """
    此题的坑在于第九行的path[:]，若不传副本则最后结果都是空
    原因在于Python中参数传递是引用传递，最后的pop()方法会对
    已经在result中的path也产生影响
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        def backtracking(n, k, start_index):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start_index, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()
        backtracking(n, k, 1)
        return result