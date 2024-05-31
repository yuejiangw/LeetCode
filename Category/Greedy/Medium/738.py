class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 贪心：一旦出现 n[i - 1] > n[i] 的情况，首先让 n[i-1] -= 1，然后把 n[i] 设成 9
        n = list(str(n))
        for i in range(len(n) - 1, 0 ,-1):
            if n[i - 1] > n[i]:
                n[i - 1] = str(int(n[i - 1]) - 1)  
                # 将修改位置后面的字符都设置为 9 因为修改前一个字符可能破坏了递增性质
                for j in range(i, len(n)):
                    n[j] = '9'
        return int(''.join(n))