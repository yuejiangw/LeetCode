from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''Greedy
        统计每个任务出现的次数，假设最高次数为 maxCount, 一共有 maxFreq 个任务都具有这个频率
        则消耗的最短时间为 (maxCount - 1) * (n + 1) + maxFreq
        这里注意，也有可能任务数较少，实际需要的时间是 len(tasks)，取二者中较大值即可    
        '''
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        maxCount = max(freq)
        maxFreq = 0
        for f in freq:
            if f == maxCount:
                maxFreq += 1
        
        return max(len(tasks), ((maxCount - 1) * (n + 1) + maxFreq))
