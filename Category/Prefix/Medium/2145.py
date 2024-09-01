from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        '''
        d[i] = h[i + 1] - h[i]

        移项有 h[i + 1] = h[i] + d[i]

        h[1] = h[0] + d[0]
        h[2] = h[1] + d[1] = h[0] + d[0] + d[1]
        h[3] = h[2] + d[2] = h[0] + d[0] + d[1] + d[2]
        h[4] = h[3] + d[3] = h[0] + d[0] + d[1] + d[2] + d[3]
        ...
        h[i] = h[0] + d[0] + d[1] + ... + d[i - 1]

        我们希望 h[i] 的值合法，则 d 的前缀和数组 d[0] + ... + d[i - 1] 加上 h[0] 的值就必须位于
        [lower, upper] 这个区间内。我们使用一个前缀和数组 prefix[i] 来记录 0-i 的前缀和，则对于每个
        i 对应的 h[0] 能取到的合法区间是 [lower - prefix[i], upper - prefix[i]]

        对 h[0] 的所有合法区间取最小交集，这个交集的长度就是答案

        T: O(N)
        S: O(1)
        '''
        l, r = lower, upper
        sum = 0
        for i in range(len(differences)):
            sum += differences[i]
            l = max(l, lower - sum)
            r = min(r, upper - sum)
        return max((r - l + 1), 0)