from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            if '0' <= log.split(' ')[1][0] <= '9':
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs = sorted(letter_logs, key=lambda s: (
            s.split(' ', 1)[1], s.split(' ', 1)[0]))
        letter_logs.extend(digit_logs)
        return letter_logs
