from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 单调递减栈
        stack = []
        res = prices[::]
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                res[idx] -= price
            stack.append(i)
        return res