from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 三种情况
        # 1. sum(gas) < sum(cost) 一定跑不完
        if sum(gas) < sum(cost):
            return -1
        
        # 2. rest[i] = gas[i] - cost[i] i 从 0 开始累加到最后一站 如果没有出现负数则说明从 0 出发即可
        min_sum = float('inf')
        curr_sum = 0
        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            curr_sum += rest
            if curr_sum < min_sum:
                min_sum = curr_sum
        if min_sum >= 0:
            return 0
        
        # 3. 如果累加最小值是负数则汽车要从非零节点出发从后向前遍历看哪个节点出发可以把这个负数填平
        for i in range(len(gas) - 1, -1, -1):
            rest = gas[i] - cost[i]
            min_sum += rest
            if min_sum >= 0:
                return i
        return -1
        