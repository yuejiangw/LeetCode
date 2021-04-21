class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''单调栈'''
        stack = []
        result = [-1] * len(nums)
        for i in range(2 * len(nums)):
            index = i % len(nums)
            if stack == []:
                stack.append((index, nums[index]))
            else:
                while len(stack) > 0 and nums[index] > stack[-1][1]:
                    stack_head = stack.pop(-1)
                    result[stack_head[0]] = nums[index]
                stack.append((index, nums[index]))
        return result