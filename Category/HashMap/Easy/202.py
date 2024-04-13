# 如果n重复出现了则说明有循环存在，一定不是快乐数

class Solution:
    def powSum(self, l: List[int]) -> int:
        sum = 0
        for n in l:
            sum += n**2
        return sum

    def isHappy(self, n: int) -> bool:
        shown = []
        while n not in shown:
            shown.append(n)
            str_n = str(n)
            nums = [int(str_n[i]) for i in range(len(str_n))]
            n = self.powSum(nums)
            if n == 1:
                return True
        return False
    
# 2024.04.12
class Solution:
    def isHappy(self, n: int) -> bool:
        # T: O(logn), S: O(logn)
        def transform(n: int) -> int:
            res = 0
            while n:
                res += pow((n % 10), 2)
                n = n // 10
            return res

        temp_results = set()
        while n != 1 and n not in temp_results:
            temp_results.add(n)
            n = transform(n)
        return True if n == 1 else False