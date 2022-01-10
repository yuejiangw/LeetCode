class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = []
        path = []
        # string split question
        # use backtracking, take a start index as the parameter
        def backtracking(start):
            # when start == len(s), return
            if start == len(num):
                # a valid sequence should have at least 3 elements
                if len(path) > 2:
                    res.append(path[:])
                return
            for i in range(start, len(num)):
                # the valid number can't have a leading '0'
                # use str(int(n)) == n to judge
                n = num[start: i + 1]
                if str(int(n)) != n:
                    break
                # the first and the second element in path does not need to follow the rule
                if len(path) < 2:
                    path.append(int(n))
                elif len(path) >= 2 and int(n) == path[-1] + path[-2]:
                    path.append(int(n))
                else:
                    continue
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return len(res) > 0
