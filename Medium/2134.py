from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        '''
                j
        nums = [0,1,0,1,1,0,0]
                          i
        len(nums) = 7
        i = 5, j = 0, window = 2 = 7 - 5 + 0
        '''
        cnt_one = sum(nums)
        n = len(nums)
        count = 0   # 记录 j 的移动次数
        i, j = 0, 0
        res = float('-inf')
        cnt_one_window = 0

        if cnt_one == n:
            return 0

        while count < n + cnt_one:
            # move right side
            c = nums[j]
            # process circular array
            j = (j + 1) % n
            count += 1
            # update window
            if c == 1:
                cnt_one_window += 1
            # move left side
            if (count < n and j - i > cnt_one) or (count >= n and j + n - i > cnt_one):
                d = nums[i]
                # process circular array
                i = (i + 1) % n
                if d == 1:
                    cnt_one_window -= 1
            # update result
            res = max(res, cnt_one_window)
        return cnt_one - res