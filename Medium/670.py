class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        贪心 + 线性扫描
        时间复杂度 O(N)
        空间复杂度 O(1), 尽管申请了一个新的数组, 但数组最大长度为 10
        """
        # 记录最后一次下标出现的位置
        last = [0] * 10
        num = list(str(num))
        for i, n in enumerate(num):
            last[int(n)] = i
        # 贪心, 从左到右扫描
        for i in range(len(num) - 1):
            for d in range(9, int(num[i]), -1):
                if last[d] > i:
                    num[i], num[last[d]] = num[last[d]], num[i]
                    return int(''.join(num))
        return int(''.join(num))
