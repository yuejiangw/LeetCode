class Solution:
    def isHappy(self, n: int) -> bool:
        # 不用 set 去重，而是基于快慢指针，有环则一定相遇
        def get_num(n):
            num = 0
            while n != 0:
                num += (n % 10) ** 2
                n = n // 10
            return num
        
        slow = get_num(n)
        fast = get_num(get_num(n))
        while slow != fast:
            slow = get_num(slow)
            fast = get_num(get_num(fast))
        return slow == 1
