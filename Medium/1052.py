from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        '''
        分两部分计算: 老板不生气时候的顾客总数 + 连续 minute window 之内可以额外获得的最大满意顾客数量
        T: O(N)
        S: O(1)
        '''
        satisfied_customer = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                satisfied_customer += customers[i]
        
        # 使用滑动窗口来计算 extra_satisfied_customer
        l = r = 0
        extra_satisfied_customer = window = 0
        while r < len(customers):
            c = customers[r]
            if grumpy[r] == 1:
                window += c
            r += 1
            if r - l < minutes:
                continue
            extra_satisfied_customer = max(extra_satisfied_customer, window)
            d = customers[l]
            if grumpy[l] == 1:
                window -= d
            l += 1
        return extra_satisfied_customer + satisfied_customer
