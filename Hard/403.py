class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # 记忆化递归：https://leetcode.cn/problems/frog-jump/solutions/603278/shou-hua-tu-jie-ji-hao-de-di-gui-ti-man-8kk2z
        """关于为什么遇到 memo 中的 key 就可以直接返回 False
        遇到 memo 中的 key 的时候说明有重复计算，那么之前的计算结果一定是 False 我们才会继续向下递归，否则程序就直接返回 True 了
        因此这里可以只用一个 set 而不用 hashMap
        """
        memo = set()

        def helper(stones, index, k) -> bool:
            # index 代表上一步所在的位置，k 代表上一跳的步长
            key = 1000 * index + k
            if key in memo:
                return False
            else:
                memo.add(key)
            for i in range(index + 1, len(stones)):
                gap = stones[i] - stones[index]
                if gap in [k - 1, k, k + 1]:
                    if helper(stones, i, gap) == True:
                        return True
                elif gap > k + 1:
                    break
            return index == len(stones) - 1

        return helper(stones, 0, 0)