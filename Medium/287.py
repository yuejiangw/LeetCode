class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 傻逼解法：暴力
        # for n in set(nums):
        #     if nums.count(n) > 1:
        #         return n

        # 正常解法：快慢指针
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow