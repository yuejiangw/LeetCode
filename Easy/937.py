from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # T: O(nlogn)
        # S: O(n)
        # 这里的 n 是 logs 里所有的 log 的内容总和
        char_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1][0].isdigit():
                digit_logs.append(log)
            else:
                char_logs.append(log)

        char_logs = sorted(char_logs, key=lambda x: (x[x.index(' ')+1:], x.split()[0]))
        return char_logs + digit_logs
