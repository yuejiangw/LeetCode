from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def lowerBound(spell, potions, success):
            l, r = 0, len(potions)
            while l < r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success: 
                    r = mid
                else:
                    l = mid + 1
            return len(potions) - l

        potions.sort()
        res = []
        for spell in spells:
            res.append(lowerBound(spell, potions, success))
        return res
