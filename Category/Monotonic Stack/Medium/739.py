from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                idx = stack.pop()[0]
                res[idx] = i - idx
            stack.append((i, temp))
        return res


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        单调栈空间复杂度优化为 O(1)
        倒序遍历，如果温度数组中的某一天温度比当前温度低，则可以借助已经计算好的 res 数组直接跳到下一个可能比当前
        天温度高的天数，而不必比较每一天的温度
        '''
        n = len(temperatures)
        res = [0] * n
        if n < 2:
            return res

        for i in range(n - 2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                else:
                    j += res[j]
            if j < n:
                res[i] = j - i
        return res