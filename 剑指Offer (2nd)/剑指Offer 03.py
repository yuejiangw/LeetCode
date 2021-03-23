class Solution:
    '''
    先排序，观察是否有相邻的元素具有一样的值，若有则代表重复
    '''
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == nums[i]:
                return pre
            pre = nums[i]