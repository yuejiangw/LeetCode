from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        if not preorder:
            return True
        stack = []
        pre_element = float('-inf')
        for i in range(len(preorder)):
            if preorder[i] <= pre_element:
                return False
            while stack and preorder[i] > stack[-1]:
                pre_element = stack.pop()
            stack.append(preorder[i])
        return True
