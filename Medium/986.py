from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []

        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            in1, in2 = firstList[i], secondList[j]
            # in1 完全包含在 in2 中
            if in1[0] >= in2[0] and in1[1] <= in2[1]:
                res.append(in1)
                i += 1
            # in2 完全包含在 in1 中
            elif in2[0] >= in1[0] and in2[1] <= in1[1]:
                res.append(in2)
                j += 1
            # in1 与 in2 没有交集且 in1 出现在 in2 后面
            elif in1[0] > in2[1]:
                j += 1
            # in1 与 in2 没有交集且 in2 出现在 in1 后面
            elif in2[0] > in1[1]:
                i += 1
            # in1 的前半部分与 in2 有交集
            elif in1[0] >= in2[0] and in1[0] <= in2[1] and in1[1] > in2[1]:
                res.append([in1[0], in2[1]])
                j += 1
            # in1 的后半部分与 in2 有交集
            elif in1[0] < in2[0] and in1[1] >= in2[0] and in1[1] <= in2[1]:
                res.append([in2[0], in1[1]])
                i += 1
            # in2 的前半部分与 in1 有交集
            elif in2[0] >= in1[0] and in2[0] <= in1[1] and in2[1] > in1[1]:
                res.append([in2[0], in1[1]])
                i += 1
            # in2 的后半部分与 in1 有交集
            elif in2[0] < in1[0] and in2[1] >= in1[0] and in2[1] <= in1[1]:
                res.append([in1[0], in2[1]])
                j += 1
        return res
