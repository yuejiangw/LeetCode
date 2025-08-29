from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        找到只包含至多1个0的最长的子数组
        '''
        l = r = 0
        res = 0
        can_delete = True
        while r < len(nums):
            c = nums[r]
            r += 1
            if c == 0:
                # 如果还有可以删除元素的机会，则继续执行
                if can_delete:
                    can_delete = False
                else:
                    # 收缩窗口找到窗口中包含的那个 0
                    while l < r and nums[l] != 0:
                        l += 1
                    # 跳过这个 0
                    l += 1
                    # 这里无需再恢复 can_delete 是因为窗口收缩的一个隐含条件是当前窗口中已经包含了2个0
            res = max(res, r - l)
        # 必须要删除一个元素
        return res - 1