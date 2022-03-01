from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # T: O(N + C), C = 120
        # S: O(C)
        """
        三个条件:
        1. ages[y] <= 0.5 * ages[x] + 7
        2. ages[y] > ages[x]
        3. ages[y] > 100 && ages[x] < 100
        可以发现, 条件3是蕴含在条件2中的, 即如果满足条件3那么一定满足条件2, 因此我们只需要关注条件1和2即可.
        当不满足条件1, 2时用户x就会向用户y发送好友请求, 即用户y需要满足:
                            0.5 * ages[x] + 7 < ages[y] <= ages[x]
        通过联立ages[y]左右的条件可知, 如果ages[y]有意义的话, 那么有 0.5 * ages[x] + 7 < ages[x],
        则 ages[x] > 14. 因此我们只需要考虑 ages[x] >= 15 的情况. 此时满足要求的 ages[y] 的范围为
        (0.5 * ages[x] + 7, ages[x]]
        """

        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        prefix = [0] * 121
        prefix[0] = count[0]
        for i in range(1, len(count)):
            prefix[i] = prefix[i - 1] + count[i]

        res = 0
        # x 要从15开始, 具体原因已经在上方注释说明
        for x in range(15, 121):
            if count[x] > 0:
                y = int(x * 0.5 + 7)
                # prefix[x] - prefix[y] 表示区间 (y, x] 的总人数
                # -1 表示去掉自己
                #  * count[x] 表示 x 年龄的人数
                res += count[x] * (prefix[x] - prefix[y] - 1)
        return res