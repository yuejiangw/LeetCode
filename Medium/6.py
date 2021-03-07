# 题目中要求的ZigZag实际上是将原字符串以'N'形来进行排列
# 通过找规律我们可以发现，每一组字符的个数为 numRows + (numRows - 2)
# 也就是 2 * numRows - 2，因此对于第i个字符，可以通过取余数的方法来
# 获得它所在的行。不过这里还有一点在于，超过 numRows 之后列数就应该反向排列
# 因此还要进行一步判断。通过一个字典来存储各个行的字符，最后依次拼接输出即可

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        lines = {}
        last_row_num = numRows - 1
        group_num = 2 * numRows - 2
        
        for i in range(len(s)):
            row_num = i % group_num
            if row_num > last_row_num:
                row_num = 2 * last_row_num - row_num
            
            if row_num in lines.keys():
                lines[row_num].append(s[i])
            else:
                lines[row_num] = [s[i]]
        
        result = ''
        for line in lines.values():
            result += ''.join(line)
        return result
