class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        '''
        可以转换为: 给你 n+1 个空余时间段，合并其中连续 k+1 个空余时间段，得到的最大长度是多少
        其中, 空余时间段长度可以为 0
        '''
        n = len(startTime)

        # 空间优化 - 使用 helper function 获取第 i 的空余时间段的长度
        def get_duration(i):
            if i == 0:
                return startTime[0]
            if i == n:
                return eventTime - endTime[-1]
            return startTime[i] - endTime[i - 1]

        # 定长滑动窗口 - 窗口长度为 k + 1
        left = right = 0
        res = window = 0
        while right < n + 1:
            window += get_duration(right)
            right += 1
            if right - left < k + 1:
                continue
            res = max(res, window)
            window -= get_duration(left)
            left += 1
        return res
        