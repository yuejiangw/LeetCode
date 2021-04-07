class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        
        # 统计连续0,1的个数
        counts = []
        i = 0
        count = 1
        while i < len(s)-1:
            if s[i+1] == s[i]:
                count += 1
            else: 
                counts.append(count)
                count = 1
            i += 1
        counts.append(count)
        
        # 相邻的0和1之间取连续字符的最小值
        i = 0
        result = 0
        while i < len(counts)-1:
            result += min(counts[i], counts[i+1])
            i += 1
        return result