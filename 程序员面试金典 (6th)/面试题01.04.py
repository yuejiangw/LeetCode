class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 满足回文串的要求如下：
        # 可能1. 所有字符都相同
        # 可能2. 所有字符出现的次数都是偶数次
        # 可能3. 只有一个字符出现奇数次，其余字符出现次数依旧是偶数
        
        s = list(s)
        
        if len(set(s)) == 1:
            return True
        
        counts = []
        for char in set(s):
            counts.append(s.count(char))
        
        odd_count = 0   # 奇数个数
        even_count = 0  # 偶数个数
        
        for num in counts:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

        if odd_count == 0 or odd_count == 1:
            return True
        else:
            return False
