from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        # Sort the costs array based on the difference between aCost and bCost,
        # the smaller the difference is, the less it will cost for this person
        # to go to a rather than b.
        sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])
        return sum([x[0] for x in sorted_costs[:n]]) + sum(x[1] for x in sorted_costs[n:])
