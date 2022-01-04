from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        result = []
        def backtracking(k, n, start_index):
            # 剪枝
            if sum(path) > n:
                return
            # 回溯终止条件
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return
            # 这里也可以应用剪枝：已知搜索空间一共只有 1-9，
            # 要求每个结果都只能包含 k 个数，则当前已经暂存
            # 的元素数量为 len(path)，还需要装入的元素数量为
            # k - len(path)。在 for 循环中，当剩余元素少于
            # 10 - (k - len(path)) + 1 时，就没有搜索的必要了
            # 因此 for 循环可以写成 for i in range(start_index, 11 - (k - len(path)))
            for i in range(start_index, 10):
                path.append(i)
                backtracking(k, n, i + 1)
                path.pop()
            return result
        backtracking(k, n, 1)
        return result