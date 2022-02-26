from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for log in logs:
            log = log.split(':')
            log_id = int(log[0])
            t = int(log[2])
            if log[1] == 'start':
                stack.append([log_id, t])
            elif log[1] == 'end':
                log_start = stack.pop()
                interval = t - log_start[1] + 1
                res[log_id] += interval
                if stack:
                    res[stack[-1][0]] -= interval
        return res