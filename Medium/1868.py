from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        # 需要动态进行解码和压缩, 否则会超时
        # T: O(M + N)
        # S: O(M + N)

        res = []
        i, j = 0, 0
        while i < len(encoded1) and j < len(encoded2):
            v1, f1 = encoded1[i]
            v2, f2 = encoded2[j]
            f = min(f1, f2)
            # 如果 res 为空或者当前的乘积与之前一个的乘积不相等, 则插入新的编码
            # 否则更新上一个编码的频率
            if not res or res[-1][0] != v1 * v2:
                res.append([v1 * v2, f])
            else:
                res[-1][1] += f

            # 根据 f1 和 f2 的数量关系更新 i 和 j
            if f1 > f:
                encoded1[i] = [v1, f1 - f]
            else:
                i += 1
            
            if f2 > f:
                encoded2[j] = [v2, f2 - f]
            else:
                j += 1
        return res
