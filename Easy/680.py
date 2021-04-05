class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        判断回文：s = s[::-1]
        '''
        if s == s[::-1]:
            return True
        i = 0
        j = len(s) - 1
        # 双指针思想：不断从两端向中间逼近
        # 遇到不相同的字符时，尝试删除任意一个
        # 之后判断剩余的中间子序列是否为回文
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                tmp1 = s[i+1:j+1]
                tmp2 = s[i:j]
                if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
                    return True
                else:
                    return False
        return True