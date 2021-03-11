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