class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # 找到 left 和 right 中间所有的素数，然后遍历作差
        # 埃氏筛
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0], is_prime[1] = False, False
            
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [x for x in range(2, n + 1) if is_prime[x]]

        primes = sieve(right)
        primes_in_range = [p for p in primes if p >= left]

        if len(primes_in_range) < 2:
            return [-1, -1]
        min_diff = primes_in_range[1] - primes_in_range[0]
        p, q = primes_in_range[0], primes_in_range[1]
        for i in range(1, len(primes_in_range) - 1):
            if primes_in_range[i + 1] - primes_in_range[i] < min_diff:
                p, q = primes_in_range[i], primes_in_range[i + 1]
                min_diff = primes_in_range[i + 1] - primes_in_range[i]
        return [p, q]