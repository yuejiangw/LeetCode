class Solution:
    def longestPalindrome(self, s: str) -> int:
        s = list(s)
        counts = []
        max_length = 0
        
        # 对s中的每一个字符出现的次数进行计数
        for character in set(s):
            counts.append(s.count(character))
        
        # 将所有出现次数为偶数次的字符都加入最后的结果
        # 对于出现次数为奇数的字符，取最大的一个放在中间
        # 其他的得减少一个变成偶数次
        i = 0
        while i < len(counts):
            if counts[i] % 2 == 0:
                max_length += counts[i]
                del counts[i]
            else:
                i += 1
        if counts:
            tmp = max(counts)
            max_length += tmp
            counts.remove(tmp)
            for c in counts:
                max_length += (c-1)
        return max_length