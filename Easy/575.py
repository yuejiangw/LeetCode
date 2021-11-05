from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        target = len(candyType) // 2
        type_num = len(set(candyType))
        return type_num if target >= type_num else target
