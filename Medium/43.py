class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # T: O(MN)
        # S: O(M + N)
        
        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1

        m, n = len(num1), len(num2)
        # 结果至多有 m + n 位 数字
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                # 乘积两位数字对应的索引位置
                p1, p2 = i + j, i + j + 1
                # 叠加到 res 上, 当前位置的 p2 就是上一层乘积的 p1
                sum = mul + res[p2]
                res[p2] = sum % 10
                res[p1] += sum // 10
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        return ''.join(map(str, res[i:]))
