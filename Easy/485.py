class Solution:
    # 解法1，计数器遍历，效率较高
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if count > max_len:
                    max_len = count
                count = 0
        if count > max_len:
            max_len = count
        return max_len
    
    # 解法2，利用Python内置方法先将整体列表转换为字符串，再以0分割，然后求最长的元素
    # 由于要进行两次for循环遍历，因此效率较低
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = ''.join([str(i) for i in nums]).split('0')
        max_len = 0
        for i in nums:
            max_len = max(max_len, len(i))
        return max_len