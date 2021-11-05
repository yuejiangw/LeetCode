from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        res = [(gas[i] - cost[i]) for i in range(len(gas))]
        min_sum = float('inf')
        curr_sum = 0
        for i in range(len(res)):
            curr_sum += res[i]
            min_sum = min(min_sum, curr_sum)

        if min_sum > 0:
            return 0

        else:
            for i in range(len(res) - 1, -1, -1):
                min_sum += res[i]
                if min_sum >= 0:
                    return i
            return -1
