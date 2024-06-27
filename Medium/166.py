class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 如果两数可以整除直接返回结果
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        res = ''
        # 如果其一为负数则加一个负号
        if numerator * denominator < 0:
            res += '-'
        
        numerator, denominator = abs(numerator), abs(denominator)
        # 计算小数点前的部分并将余数赋值给 numerator
        res += str(numerator // denominator) + '.'
        numerator %= denominator
        # 使用哈希表来记录余数最早在什么位置出现的，一旦出现相同余数则把出现位置到当前位置之间的字符串摘出来作为循环部分
        remainder = {}
        while numerator != 0:
            # 记录余数所在答案的位置并继续模拟除法运算
            remainder[numerator] = len(res)
            numerator *= 10
            res += str(numerator // denominator)
            numerator %= denominator
            # 如果当前余数在之前出现过，则将 [出现位置 到 当前位置] 的部分拿出来作为循环部分
            if numerator in remainder:
                start = remainder[numerator]
                return f'{res[0: start]}({res[start:]})' 
        return res