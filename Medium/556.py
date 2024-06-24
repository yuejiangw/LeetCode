class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 和 31 - 下一个排列一样，Greedy
        # 找到左边一个较小的数和右边的一个较大的数并交换，要求较小数尽可能靠右，较大数尽可能靠左
        nums = list(str(n))
        i = len(nums) - 2
        # 找左边较小数
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1
        # 找右边较大数
        j = len(nums) - 1
        while j > i and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        res = int(''.join(nums))
        return res if res < 2 ** 31 else -1
        