class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = [1, 1]
        next_fib = fibs[0] + fibs[1]
        # Get all the fib numbers that are less than or equal to k.
        while next_fib <= k:
            fibs.append(next_fib)
            next_fib = fibs[-1] + fibs[-2]

        res = 0
        # Iterate the candidate fib numbers from end to start,
        # and choose the larger fib number as much as possible.
        for i in range(len(fibs) - 1, -1, -1):
            res += k // fibs[i]
            k %= fibs[i]
            if k == 0:
                break
        return res
