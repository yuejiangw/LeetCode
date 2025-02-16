from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # edge case
        if not n:
            return True
        if len(flowerbed) <= 2 and sum(flowerbed) >= 1:
            return n == 0

        # common cases - len(flowerbed) >= 3
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                elif i == 0:
                    if flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if n == 0:
                return True

        return False

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            new_num = 1 if flowerbed[0] == 0 else 0
        elif len(flowerbed) == 2:
            new_num = 1 if flowerbed == [0, 0] else 0
        else:
            new_num = 0
            if flowerbed[:2] == [0, 0]:
                new_num += 1
                flowerbed[0] = 1
            for i in range(1, len(flowerbed)-1):
                if flowerbed[i-1: i+2] == [0, 0, 0]:
                    new_num += 1
                    flowerbed[i] = 1
            if flowerbed[-2:] == [0, 0]:
                new_num += 1
                flowerbed[-1] = 1
        return new_num >= n