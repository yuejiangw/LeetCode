from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        """
        dfs 的迭代写法，每进入到下一层，相当于把当前的 num *= 10，每返回上一层，相当于
        把当前的 num //= 10. num 初始值为1，先不断 * 10 并添加以当前最高位数字为首的数字
        到结果中，再一口气退出到最底层，num += 1
        """
        res = []
        num = 1
        while len(res) < n:
            while num <= n:
                res.append(num)
                num *= 10
            while num % 10 == 9 or num > n:
                num //= 10
            num += 1
        return res
