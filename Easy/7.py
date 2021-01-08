# 此题的坑在于限制了整数的范围，而python并不检查此范围
# 因此需要手动加以约束

class Solution:
    def reverse(self, x: int) -> int:
        strX = str(x)
        if strX[0] == '-':
            tmp = strX[::-1]
            result = int('-' + tmp[:-1])
        else:
            result =  int(strX[::-1])
        return result if -2 ** 31 < result < 2 ** 31 - 1 else 0