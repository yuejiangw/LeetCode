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
            # 剪枝优化策略：当前已经暂存的元素数量为 len(path)，则还要
            # 取 k - len(path) 个元素，所以在进行 for 循环的时候，应该
            # 保证剩余的元素大于等于 k - len(path)。已知总元素个数为 n，
            # 因此当 i <= n - (k - len(path)) + 1 的时候才有搜索的必要
            for i in range(start_index, n - (k - len(path)) + 2):
                path.append(i)
                backtracking(n, k, i + 1)
                path.pop()
        backtracking(n, k, 1)
        return result