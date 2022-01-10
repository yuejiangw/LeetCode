class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = []
        path = []
        # string split question
        # use backtracking, take a start index as the parameter
        def backtracking(start):
            # when start == len(s), return
            if start == len(num):
                if len(path) > 2:
                    res.append(path[:])
                return
            for i in range(start, len(num)):
                n = num[start: i + 1]
                if len(path) < 2 and str(int(n)) == n:
                    path.append(int(n))
                elif len(path) >= 2 and str(int(n)) == n and int(n) == path[-1] + path[-2]:
                    path.append(int(n))
                else:
                    continue
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return len(res) > 0
