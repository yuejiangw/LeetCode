class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        '''
        通过 binary search 来确定 nums[index] 最大可以多大
        类似于 1011
        '''
        def getMinSum(val, index, n, maxSum):
            # Greedy, 获取 sum(nums) 的最小值
            # 不能用遍历的方法一个个算，只能用数学法，否则会超时
            count = 0
            # left
            if val > index:
                # 可以一直减
                count += (val + val - index) * (index + 1) // 2
            else:
                # 需要用 1 填
                count += (val + 1) * val // 2 + (index - val + 1)
            # right
            if val > n - index - 1:
                # 可以一直减
                count += (val + (val - (n - index - 1))) * (n - index) // 2
            else:
                # 需要用 1 填
                count += (val + 1) * val // 2 + n - index - val
            
            # 多加了一个 val 要减去
            return count - val
        
        # T: O(log(maxSum))
        # S: O(1)
        if n == 1:
            return maxSum
        i, j = 1, maxSum
        while i < j:
            mid = i + (j - i) // 2
            min_bound = getMinSum(mid, index, n, maxSum)
            if min_bound <= maxSum:
                i = mid + 1
            else:
                j = mid
        return i - 1
        