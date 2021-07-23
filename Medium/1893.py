class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        def cover(r: List[int], i: int) -> bool:
            return i >= r[0] and i <= r[1]

        ranges = sorted(ranges, key=lambda x : x[1])
        print(ranges)
        for i in range(left, right + 1):
            flag = False
            for r in ranges:
                if cover(r, i):
                    flag = True
            if not flag:
                return False
        return True