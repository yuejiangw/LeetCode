from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        stack = []
        count1 = 0
        # 正向单调栈: 非递减
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1]:
                count1 += 1
                stack.pop()
            stack.append(nums[i])

        stack.clear()

        count2 = 0
        # 反向单调栈: 非递增
        # 加入反向单调栈的原因: 避免 [5, 7, 1, 8] 这种情况的误判
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > stack[-1]:
                count2 += 1
                stack.pop()
            stack.append(nums[i])

        return min(count1, count2) <= 1
