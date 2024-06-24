class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # 和 31 - 下一个排列一样，Greedy
        # 找到左边一个较小的数和右边的一个较大的数并交换，要求较小数尽可能靠右，较大数尽可能靠左
        nums = list(str(n))
        i = len(nums) - 2
        # 倒序遍历查找到第一个降序的元素
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1
        # 倒序遍历查找第一个大于降序元素的元素
        j = len(nums) - 1
        while j > i and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        # 对第一个降序之后升序排列
        # 这里隐含的是 nums[i + 1:] 一定是一个降序序列，这是由第一遍倒序查找的条件决定的
        # 降序的数字排列是从大到小，把它们变成从小到大才可以保证是 next greater num
        nums[i + 1:] = nums[i + 1:][::-1]
        res = int(''.join(nums))
        return res if res < 2 ** 31 else -1
        