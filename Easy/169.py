from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = Counter(nums)
        max_num = max(dic.values())
        for k, v in dic.items():
            if v == max_num:
                return k