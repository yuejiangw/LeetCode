from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # T: O(N)
        # S: O(N)
        stack = []
        for asteroid in asteroids:
            while stack and (stack[-1] > 0 and asteroid < 0) \
                and (abs(stack[-1]) < abs(asteroid)):
                stack.pop()
            if stack and stack[-1] > 0 and stack[-1] + asteroid == 0:
                stack.pop()
                continue
            if stack and stack[-1] > 0 and asteroid < 0 and abs(stack[-1]) > abs(asteroid):
                continue
            stack.append(asteroid)
        return stack