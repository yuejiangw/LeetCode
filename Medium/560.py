from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        sum 的含义是前缀和，当 sum-k 出现在哈希表中的时候，说明之前存在一个前缀和 sum'，使得 sum'=sum-k
        这意味着从 sum' 到当前 sum 之前的子数组的和为 k，因为 sum - sum' = k
        所以每当我们遇到 sum-k 出现在哈希表中的时候，就可以更新 res
        '''
        count = {0: 1}
        sum = 0
        res = 0
        for num in nums:
            sum += num
            if (sum - k) in count:
                res += count[sum-k]
            if sum in count:
                count[sum] += 1
            else:
                count[sum] = 1
        return res
