class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        results = []
        i = 1
        while i < target - 1:
            tmp = [i]
            j = i + 1
            tmp.append(j)
            summation = sum(tmp)
            while summation < target:
                j += 1
                tmp.append(j)
                summation = sum(tmp)
            if summation == target:
                results.append(tmp)
            i += 1
        return results