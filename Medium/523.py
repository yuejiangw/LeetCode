from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        val_index = {}
        for i in range(len(prefix)):
            val = prefix[i] % k
            # 如果 val 还未在哈希表中出现过, 则记录它第一次出现的下标
            # 这样做的目的是保证下标之差尽可能的大, 所以相同 val 的 index 不会被更新
            if val not in val_index:
                val_index[val] = i
        
        for i in range(1, len(prefix)):
            need = prefix[i] % k
            if need in val_index:
                if i - val_index[need] >= 2:
                    return True
        return False