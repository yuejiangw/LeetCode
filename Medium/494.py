class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        由于可以任意加 +/- 号，所以原题等价于：在nums中找到一个正子集和负子集，
        使两个子集的和等于target。假设正子集的和为x，则负子集的和为sum(nums) - x，
        题目要求x - [sum(nums) - x] == target，则x = [sum(nums) + target] // 2。
        
        所以题目可以转换为一个背包问题：给定一个数组nums，想要从中找出一个和为x的子集，
        一共有几种方法？
        """
        # 如果x不能被2整除，则没有方法
        if (sum(nums) + target) % 2 != 0:
            return 0
        
        # 如果取全集也仍旧达不到target，则没有方法
        if sum(nums) < target or -sum(nums) > target:
            return 0
        
        bag_weight = (sum(nums) + target) // 2
        
        dp = [0 for i in range(bag_weight + 1)]
        dp[0] = 1

        # dp[j]的含义为，在nums中取下标范围为[0:i]的子数组时，
        # 填满容量为j的背包有dp[j]种方法
        for i in range(len(nums)):
            j = bag_weight
            while j >= nums[i]:
                dp[j] += dp[j - nums[i]]
                j -= 1
        return dp[bag_weight]