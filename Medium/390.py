class Solution:
    def lastRemaining(self, n: int) -> int:
        # 无论从左到右还是从右到左，每次都会删除一半数字
        # 从左到右，每次都会删除第一个数字
        # 从右到左，只有数组长度为奇数才会删除第一个数字
        remain = n
        flag = True
        res = 1
        step = 1
        while remain > 1:
            # 从左到右，或者剩余个数为奇数
            if flag or remain % 2 == 1:
                res += step
            flag = not flag
            step *= 2
            remain //= 2
        return res
