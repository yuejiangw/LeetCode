from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        '''
        双指针，对于两个 list 中当前的元素对，取最大下界和最小上界并通过大小判断是否有交集，
        对于移动指针，哪个 list 中当前元素对的上界较小就移动谁的指针，因为该 list 中的下一个元素可能与另一个 list 的当前元素对依旧相交
        T: O(M + N)
        S: O(M + N)
        '''
        res = []
        if len(firstList) == 0 or len(secondList) == 0:
            return res

        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                res.append([start, end])
            
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return res


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
