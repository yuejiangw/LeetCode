class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0
        
        symbol = None        
        res = 0
        i = 0
        if s[i] == '+' or s[i] == '-':
            symbol = s[i]
            i += 1
        while i < len(s):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else: 
                break
            i += 1

        if res == 0:
            return res
        
        if symbol == '-':
            res = -res

        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else:
            return res
        

class Solution:
    def isDigit(self, c):
        return (c >= '0' and c <= '9')
    
    def myAtoi(self, s: str) -> int:
        result = ''

        # 删除开头的空格
        tmp = s.strip().split(' ')[0]

        # 空字符
        if tmp == '':
            return 0
        # 仅由一个非数字字符组成
        elif len(tmp) == 1 and not self.isDigit(tmp[0]):
            return 0
        # 非法字符开头
        elif not self.isDigit(tmp[0]) and tmp[0] != '-' and tmp[0] != '+':
            return 0
        
        # 开头是+或-
        elif (tmp[0] == '-' or tmp[0] == '+'):
            # 继续读后续字符直到为非数字
            i = 1
            while (self.isDigit(tmp[i]) and i < len(tmp)-1):
                i += 1
            if self.isDigit(tmp[i]):
                i += 1
            str_result = tmp[:i]
            # 防止+/-连续出现
            if len(str_result) == 1:
                return 0
            
            result = str_result
        # 开头是数字
        else:
            # 继续读后续字符直到为非数字
            i = 0
            while (self.isDigit(tmp[i]) and i < len(tmp)-1):
                i += 1
            if self.isDigit(tmp[i]):
                i += 1
            result = tmp[:i]

        result = int(result)

        if result < -pow(2, 31):
            return -pow(2, 31)
        elif result > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return result

class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        n = len(s)

        while idx < n and s[idx] == ' ':
            idx += 1
        
        if idx == n:
            return 0

        # Judge if s is a positive or negative number.
        is_negative = False
        if s[idx] == '-':
            is_negative = True
            idx += 1
        elif s[idx] == '+':
            idx += 1
        elif not s[idx].isdigit():
            return 0
        
        res = 0
        while idx < n and s[idx].isdigit():
            digit = int(s[idx])
            res = res * 10 + digit
            idx += 1
            if not is_negative and res > 2**31 - 1:
                return 2** 31 - 1
            elif is_negative and -res < -2**31:
                return -2**31
        return -res if is_negative else res