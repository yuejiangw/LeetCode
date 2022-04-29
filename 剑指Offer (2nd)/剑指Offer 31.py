from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # T: O(N)
        # S: O(N)
        # 用一个栈模拟入栈操作，同时用一个指针指向 popped 序列中的目标元素，当栈顶元素与 popped 序列中
        # 对应元素相同时出栈，最后判断指针是否来到 popped 序列的末尾即可
        i = 0
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(popped)