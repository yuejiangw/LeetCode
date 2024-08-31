from typing import List

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        # simulation
        t = 1
        while t <= max(memory1, memory2):
            if memory1 < memory2:
                memory2 -= t
            else:
                memory1 -= t
            t += 1
        return [t, memory1, memory2]