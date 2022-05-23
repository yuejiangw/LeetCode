class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """思路: 双指针
        L 只能向左走, R 只能向右走, 并且 L 和 R 不能交叉走, 因此 start 和 end 应该满足
        如下性质:
        1. 去掉 X 之后剩余的字符串应该相同
        2. 如果 start 中当前下标对应的是 L, 则在 end 中对应的下标应该 <= start 中的下标
        3. 如果 start 中当前下标对应的是 R, 则在 end 中对应的下标应该 >= start 中的下标
        """
        # T: O(N)
        # S: O(1)
        i, j = 0, 0
        while True:
            while i < len(start) and start[i] == 'X':
                i += 1
            while j < len(end) and end[j] == 'X':
                j += 1
            if i >= len(start) and j >= len(end):
                return True
            if i >= len(start) or j >= len(end):
                return False
            if start[i] != end[j]:
                return False
            if (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False
            i += 1
            j += 1
        return True
